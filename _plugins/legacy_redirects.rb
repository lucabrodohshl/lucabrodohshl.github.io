# Redirect stubs for the former GitHub Pages project-site URLs.
#
# Until October 2026 the site was served at
#   https://lucabrodohshl.github.io/lucabrodohshl/...
# It now lives at the domain root. For every HTML page and publication page,
# this generator writes /lucabrodohshl/<same path>/index.html containing an
# immediate meta refresh and a canonical link to the new URL, so old links and
# indexed URLs keep working and search engines transfer them to the new ones.
# The stubs are marked noindex and are not listed in the sitemap.
module LegacyRedirects
  PREFIX = "lucabrodohshl".freeze

  class Generator < Jekyll::Generator
    safe true
    priority :lowest

    def generate(site)
      root = site.config["url"].to_s + site.config["baseurl"].to_s
      targets = site.pages.select do |page|
        page.html? && !page.data["noindex"] && !page.url.start_with?("/#{PREFIX}/")
      end
      targets += site.collections["publications"].docs
      targets += site.collections["tutorials"].docs

      targets.each do |item|
        stub = Jekyll::PageWithoutAFile.new(site, site.source, File.join(PREFIX, item.url), "index.html")
        stub.data["layout"] = "none"
        stub.data["noindex"] = true
        stub.content = stub_html(root + item.url)
        site.pages << stub
      end
    end

    private

    def stub_html(target)
      <<~HTML
        <!doctype html>
        <html lang="en">
        <head>
        <meta charset="utf-8">
        <title>Page moved</title>
        <link rel="canonical" href="#{target}">
        <meta name="robots" content="noindex">
        <meta http-equiv="refresh" content="0; url=#{target}">
        </head>
        <body>
        <p>This page has moved to <a href="#{target}">#{target}</a>.</p>
        </body>
        </html>
      HTML
    end
  end
end
