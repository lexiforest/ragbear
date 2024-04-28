from ragbear.extract import extract_md_from_html


def test_extract_md_from_html():
    html = """
    <h1>A New Era for Mixed Reality</h1>
    <p class="new">Today we’re taking the next step toward our vision for a more open computing platform for the metaverse. We’re opening up the operating system powering our Meta Quest devices to third-party hardware makers, giving more choice to consumers and a larger ecosystem for developers to build for. We’re working with leading global technology companies to bring this new ecosystem to life and making it even easier for developers to build apps and reach their audiences on the platform.</p>
    """
    md = """A New Era for Mixed Reality
===========================


Today we’re taking the next step toward our vision for a more open computing platform for the metaverse. We’re opening up the operating system powering our Meta Quest devices to third-party hardware makers, giving more choice to consumers and a larger ecosystem for developers to build for. We’re working with leading global technology companies to bring this new ecosystem to life and making it even easier for developers to build apps and reach their audiences on the platform.


"""
    extracted = extract_md_from_html(html)

    assert extracted == md
