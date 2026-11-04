"""Generate the one-page, selectable-text CV PDF used by the Sphinx site.

Run with a Python environment that has ReportLab installed:
    python tools/generate_cv.py
"""

from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    HRFlowable,
    KeepTogether,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "docs" / "files" / "Kapsalis_Christoforos_CV.pdf"
BLUE = colors.HexColor("#2859a6")
INK = colors.HexColor("#202124")
MUTED = colors.HexColor("#5f6368")


styles = getSampleStyleSheet()
styles.add(
    ParagraphStyle(
        name="CVName", parent=styles["Normal"], fontName="Helvetica-Bold",
        fontSize=18, leading=20, alignment=TA_CENTER, textColor=BLUE,
        spaceAfter=2,
    )
)
styles.add(
    ParagraphStyle(
        name="CVContact", parent=styles["Normal"], fontName="Helvetica",
        fontSize=8.6, leading=11, alignment=TA_CENTER, textColor=INK,
    )
)
styles.add(
    ParagraphStyle(
        name="CVProfile", parent=styles["Normal"], fontName="Helvetica",
        fontSize=8.9, leading=11.4, alignment=TA_CENTER, textColor=MUTED,
        spaceBefore=2, spaceAfter=3,
    )
)
styles.add(
    ParagraphStyle(
        name="CVSection", parent=styles["Normal"], fontName="Helvetica-Bold",
        fontSize=10, leading=12, textColor=BLUE, spaceBefore=4.5,
        spaceAfter=1.5,
    )
)
styles.add(
    ParagraphStyle(
        name="CVRole", parent=styles["Normal"], fontName="Helvetica-Bold",
        fontSize=8.9, leading=10.6, textColor=INK,
    )
)
styles.add(
    ParagraphStyle(
        name="CVDate", parent=styles["Normal"], fontName="Helvetica-Oblique",
        fontSize=8.4, leading=10.2, alignment=TA_RIGHT, textColor=MUTED,
    )
)
styles.add(
    ParagraphStyle(
        name="CVSubline", parent=styles["Normal"], fontName="Helvetica-Oblique",
        fontSize=8.5, leading=10.2, textColor=MUTED, spaceAfter=0.5,
    )
)
styles.add(
    ParagraphStyle(
        name="CVBody", parent=styles["Normal"], fontName="Helvetica",
        fontSize=8.55, leading=10.6, textColor=INK, spaceAfter=1,
    )
)
styles.add(
    ParagraphStyle(
        name="CVBullet", parent=styles["CVBody"], leftIndent=9,
        firstLineIndent=-7, spaceAfter=0.4,
    )
)


def paragraph(text, style="CVBody"):
    return Paragraph(text, styles[style])


def section(title):
    return [
        paragraph(title.upper(), "CVSection"),
        HRFlowable(width="100%", thickness=0.7, color=BLUE, spaceAfter=3),
    ]


def role(title, date, subline=None, bullets=()):
    heading = Table(
        [[paragraph(title, "CVRole"), paragraph(date, "CVDate")]],
        colWidths=[4.95 * inch, 2.1 * inch],
        hAlign="LEFT",
    )
    heading.setStyle(
        TableStyle([
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("LEFTPADDING", (0, 0), (-1, -1), 0),
            ("RIGHTPADDING", (0, 0), (-1, -1), 0),
            ("TOPPADDING", (0, 0), (-1, -1), 0),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
        ])
    )
    content = [heading]
    if subline:
        content.append(paragraph(subline, "CVSubline"))
    content.extend(paragraph(f"- {bullet}", "CVBullet") for bullet in bullets)
    content.append(Spacer(1, 2))
    return KeepTogether(content)


story = [
    paragraph("CHRISTOFOROS KAPSALIS", "CVName"),
    paragraph(
        'Agrinio, Greece &nbsp;|&nbsp; +30 698 826 3291 &nbsp;|&nbsp; '
        '<link href="mailto:ch.kapsalis@outlook.com" color="#2859a6">'
        'ch.kapsalis@outlook.com</link> &nbsp;|&nbsp; '
        '<link href="https://linkedin.com/in/christoforos-kapsalis" color="#2859a6">'
        'LinkedIn</link> &nbsp;|&nbsp; '
        '<link href="https://github.com/C-Kapsalis" color="#2859a6">GitHub</link>',
        "CVContact",
    ),
    paragraph(
        "Technical author and product-minded engineer working across software, data, and marketing.",
        "CVProfile",
    ),
]

story += section("Experience")
story.append(
    role(
        "Canonical - Technical Author (incoming)",
        "Starting 9 Nov 2026",
        "Charm Engineering",
    )
)
story.append(
    role(
        "Maya Insights - Shopify App: Product and Marketing",
        "Nov 2026 - Present",
        "Contract | Remote",
    )
)
story.append(
    role(
        "Maya Insights - Marketing Engineer",
        "Apr 2024 - Nov 2026",
        "Full-time | Remote",
        [
            "Owned the Maya MCP server prototype and designed its LLM-to-semantic-model contract: intent classification, metadata retrieval, and automatic DAX query generation.",
            "Moved Power BI models to TMDL and unified advertising, CRM, and web data. Built retention dashboards and automated lead workflows that identified a 15% churn-risk segment and doubled lead conversion.",
        ],
    )
)
story.append(
    role(
        "Syracuse University - Whitman School of Management",
        "Jan 2026 - May 2026",
        "Research Assistant, Marketing | Teaching Assistant, Finance",
        [
            "Built a longitudinal research panel and applied fixed-effects methods to study non-profit and church retention and engagement.",
            "Supported the graduate Data Analysis course through office hours, grading, and instruction.",
        ],
    )
)
story.append(
    role(
        "Wikifarmer - Marketing and Analytics Specialist",
        "Jun 2023 - Mar 2024",
        "Athens, Greece",
        [
            "Cut customer acquisition cost 18%, lifted email open rate 17%, and launched a blog that drove 50% of newsletter signups within three months.",
            "Built Power BI KPI dashboards and led email campaigns to 10,000+ contacts; wrote company thought leadership and press pieces.",
        ],
    )
)
story.append(
    role(
        "Wikifarmer - Pre-Sales Executive Intern",
        "Mar 2023 - Jun 2023",
        "Athens, Greece",
        ["Supported DACH lead generation, HubSpot data quality, and email-marketing automation."],
    )
)

story += section("Selected open-source work")
story.append(
    paragraph(
        "<b>AI skills:</b> Devil's Analyst (marketing analytics), Second Read (editing), Swift PBI (Power BI), and Value Pricing (pricing research). "
        "<b>CLI tools:</b> tmdl-preflight, pbip-model-forge, tmdl-drift-doctor, and pbi-plot-styler. "
        "<b>SaaS:</b> Second Read Studio, an editorial review workspace in beta. "
        "<b>Open source:</b> merged documentation contributions in Ulwazi, Launchpad, Canonical robotics, and Diataxis.",
    )
)

story += section("Education")
story.append(
    paragraph(
        "<b>Syracuse University, Whitman</b> - M.S. Marketing (STEM), Aug 2025-May 2026; "
        "GPA 4.0/4.0; Fulbright Scholar and Beta Gamma Sigma.",
    )
)
story.append(
    paragraph(
        "<b>American College of Greece</b> - M.S. Data Science, Sep 2023-Jul 2025; "
        "GPA 4.0/4.0; Presidential Scholarship.",
    )
)
story.append(
    paragraph(
        "<b>Athens University of Economics and Business</b> - B.S. Economics, "
        "Sep 2019-Jul 2023; 9.44/10 (Excellent).",
    )
)

story += section("Skills and certifications")
story.append(
    paragraph(
        "<b>Technical writing:</b> Sphinx, reStructuredText, Diataxis, Git, CI. "
        "<b>AI and software:</b> Python, SQL, MCP, agent skills and plugins. "
        "<b>Data and BI:</b> Power BI, DAX, TMDL, BigQuery, R, machine learning. "
        "<b>Marketing:</b> GA4, HubSpot, SEM, SEO, email and paid social. "
        "<b>Certifications:</b> Microsoft Excel Associate (MO-210), Google Analytics, DataCamp R, University of Amsterdam Communication Science.",
    )
)


document = SimpleDocTemplate(
    str(OUTPUT),
    pagesize=letter,
    rightMargin=0.64 * inch,
    leftMargin=0.64 * inch,
    topMargin=0.34 * inch,
    bottomMargin=0.34 * inch,
    title="Christoforos Kapsalis - CV",
    author="Christoforos Kapsalis",
    subject="Technical writing, AI skills, developer tools, and marketing engineering",
)
document.build(story)
print(OUTPUT)
