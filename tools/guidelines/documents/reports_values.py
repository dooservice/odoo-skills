"""The parts of `reports.md` that differ per version: tags, report types, QWeb and the engine."""

from __future__ import annotations

from ..version import OdooVersion


class ReportValues:
    def values(self, version: OdooVersion) -> dict[str, str]:
        return {
            "report_tag": version.pick(
                v16=" The `<report>`\nshortcut tag still loads but is deprecated: write the `<record>`.",
                v17_=" There is no `<report>`\ntag: write the `<record>`.",
            ),
            "report_types": version.pick(
                v16_19="`qweb-pdf` (a PDF rendered by wkhtmltopdf), `qweb-html` (opened in\n"
                "  the browser) or `qweb-text` (plain text).",
                v20="`qweb-pdf` (a PDF rendered by the database's default engine),\n"
                "  `qweb-pdf-wkhtmltopdf` or `qweb-pdf-paper-muncher` (a PDF rendered by that engine),\n"
                "  `qweb-html` (opened in the browser) or `qweb-text` (plain text).",
            ),
            "groups_field": version.pick(v16_18="groups_id", v19_="group_ids"),
            "esc": version.pick(
                v16_19="`t-esc` and `t-raw` are deprecated: write\n"
                "  `t-out`, and instead of `t-raw` pass a `Markup` value built in Python.",
                v20="`t-esc` and `t-raw` are no longer\n"
                "  directives: QWeb ignores them with a warning and prints nothing. Write `t-out`.",
            ),
            "tcall": self.tcall(version),
            "engine": self.engine(version),
        }

    def tcall(self, version: OdooVersion) -> str:
        attributes = (
            "- Pass values to a sub-template as attributes of the `t-call` element, which must be\n"
            "  a `<t>`: `<t t-call=\"library.report_book_line\" show_price=\"True\" title.f=\"Book {{o.name}}\"/>`\n"
            "  (`.f` marks a format string). "
        )
        return version.pick(
            v16_18="- Pass values to a sub-template with `t-set` inside the `t-call` body:\n"
            "  `<t t-call=\"library.report_book_line\"><t t-set=\"show_price\" t-value=\"True\"/></t>`;\n"
            "  the rest of the body reaches the sub-template as `0` (`<t t-out=\"0\"/>`).",
            v19=attributes + "A `t-set` inside the body still reaches the sub-template\n"
            "  when the element has no such attribute, but that form is deprecated. The body\n"
            "  reaches the sub-template as `0` (`<t t-out=\"0\"/>`).",
            v20=attributes + "A `t-set` inside the body no longer reaches the\n"
            "  sub-template; `odoo-bin upgrade_code` rewrites that old form. The body reaches the\n"
            "  sub-template as `0` (`<t t-out=\"0\"/>`).",
        )

    def engine(self, version: OdooVersion) -> str:
        wkhtmltopdf = (
            "- wkhtmltopdf renders the report's HTML with an old WebKit: the HTML preview\n"
            "  (`qweb-html`, or the browser) shows what a modern browser does, not what the PDF\n"
            "  shows. Check every layout change in the printed PDF.\n"
            "- wkhtmltopdf loads the report's CSS and images from the server at the `report.url`\n"
            "  system parameter, or `web.base.url` when it is unset: when the Odoo machine cannot\n"
            "  reach that URL, PDFs print without styles.\n"
            "- With `--workers=1` no PDF prints: the only worker waits for wkhtmltopdf while\n"
            "  wkhtmltopdf asks the server for the assets. Run with `--workers=0` or at least 2."
        )
        return version.pick(
            v16_19=wkhtmltopdf,
            v20="- `qweb-pdf` uses the engine named by the `report.pdf_engine_default` system\n"
            "  parameter: `wkhtmltopdf`, set by `base_report_wkhtmltox`, which installs\n"
            "  automatically. `base_report_paper_muncher` adds Odoo's own engine, chosen per report\n"
            "  with `qweb-pdf-paper-muncher`; a module whose report names an engine depends on the\n"
            "  module that provides it.\n" + wkhtmltopdf,
        )
