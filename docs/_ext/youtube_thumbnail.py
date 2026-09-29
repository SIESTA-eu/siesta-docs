"""Sphinx directive that turns a YouTube URL into a linked thumbnail."""

from urllib.parse import parse_qs, urlparse

from docutils import nodes
from docutils.parsers.rst import Directive


class YouTubeThumbnail(Directive):
    """Display the thumbnail for a YouTube video, linked to its URL."""

    required_arguments = 1
    optional_arguments = 0
    has_content = False

    def run(self):
        video_url = self.arguments[0].strip()
        parsed_url = urlparse(video_url)
        host = parsed_url.netloc.lower().removeprefix("www.")

        video_id = None
        if host == "youtu.be":
            video_id = parsed_url.path.strip("/").split("/")[0]
        elif host in {"youtube.com", "m.youtube.com", "youtube-nocookie.com"}:
            if parsed_url.path == "/watch":
                video_id = parse_qs(parsed_url.query).get("v", [None])[0]
            elif parsed_url.path.startswith(("/embed/", "/shorts/", "/live/")):
                video_id = parsed_url.path.split("/")[2]

        if not video_id:
            raise self.error(
                "Expected a YouTube video URL, such as "
                "https://www.youtube.com/watch?v=VIDEO_ID"
            )

        image = nodes.image(
            uri=f"https://img.youtube.com/vi/{video_id}/0.jpg",
            alt="Watch the video on YouTube",
        )
        link = nodes.reference(refuri=video_url)
        link += image
        return [link]


def setup(app):
    app.add_directive("youtube-thumbnail", YouTubeThumbnail)
    return {"version": "1.0", "parallel_read_safe": True}
