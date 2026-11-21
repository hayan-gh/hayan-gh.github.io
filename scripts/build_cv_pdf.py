#!/usr/bin/env python3
"""Build the public CV PDF from the confirmed CV text.

The phone number that appears on the source CV is omitted here so the
downloadable file on the public site does not publish it.
"""

from pathlib import Path

from fpdf import FPDF

ROOT = Path(__file__).resolve().parents[1]
FONTS = ROOT / "assets" / "fonts"
OUT = ROOT / "cv" / "Hayan_Aljabr_CV_EN.pdf"


class CV(FPDF):
    def footer(self):
        self.set_y(-12)
        self.set_font("Inter", "", 8)
        self.set_text_color(90, 98, 108)
        self.cell(0, 6, f"Hayan Aljabr  ·  hayan.aljaber@gmail.com  ·  {self.page_no()}/{{nb}}", align="L")


def block(pdf, height, text, font, size, style="", color=(27, 36, 48)):
    pdf.set_x(pdf.l_margin)
    pdf.set_font(font, style, size)
    pdf.set_text_color(*color)
    pdf.multi_cell(0, height, text, new_x="LMARGIN", new_y="NEXT")


def heading(pdf, text):
    pdf.ln(3)
    block(pdf, 7, text, "Serif", 13, "B", (14, 95, 92))
    pdf.set_draw_color(221, 212, 196)
    y = pdf.get_y()
    pdf.line(16, y, 194, y)
    pdf.ln(3)


def role(pdf, title, org, meta):
    block(pdf, 6, title, "Serif", 12, "B")
    block(pdf, 5.5, org, "Inter", 10.5, "B")
    if meta:
        block(pdf, 5, meta, "Inter", 9.5, "", (92, 101, 112))
    pdf.ln(1)


def bullets(pdf, items):
    for item in items:
        pdf.set_font("Inter", "", 10)
        pdf.set_text_color(27, 36, 48)
        pdf.set_x(18)
        pdf.multi_cell(0, 4.8, "•  " + item, new_x="LMARGIN", new_y="NEXT")
        pdf.ln(1.1)


def main():
    pdf = CV(format="A4")
    pdf.set_auto_page_break(auto=True, margin=16)
    pdf.alias_nb_pages()
    pdf.add_font("Inter", "", str(FONTS / "Inter-Regular.ttf"))
    pdf.add_font("Inter", "B", str(FONTS / "Inter-SemiBold.ttf"))
    pdf.add_font("Serif", "B", str(FONTS / "NotoSerif-Bold.ttf"))
    pdf.add_page()
    block(pdf, 10, "Hayan Aljabr", "Serif", 22, "B")
    block(pdf, 6, "Software Engineer | Python Backend & Odoo ERP", "Inter", 11, "B", (14, 95, 92))
    pdf.ln(1)
    block(
        pdf,
        5,
        "Damascus, Syria   ·   hayan.aljaber@gmail.com\n"
        "linkedin.com/in/hayan-aljabr   ·   github.com/hayan-gh   ·   Open to relocation",
        "Inter",
        9.5,
        "",
        (92, 101, 112),
    )
    pdf.ln(2)
    block(
        pdf,
        5.2,
        "Python backend engineer building FastAPI and Flask services on PostgreSQL for "
        "digital wallets and banking APIs. Work includes customer, merchant and corporate "
        "onboarding with Keycloak, transaction lifecycles around persisted payment intents "
        "and payment state machines, server-issued idempotency references, reconciliation of "
        "ambiguous ledger outcomes, and asynchronous processing with Celery and Redis.",
        "Inter",
        10.5,
    )

    heading(pdf, "Experience")
    role(pdf, "Software Engineer", "rmz", "Nov 2025 – Present  ·  Full-time  ·  On-site, Damascus")
    bullets(
        pdf,
        [
            "Started the Wafra Pay wallet backend (FastAPI, SQLAlchemy, PostgreSQL) as a modular monolith with Alembic: registration, OTP authentication, wallet provisioning, P2P transfers, QR merchant payments, and bill payments on an Apache Fineract ledger.",
            "Designed transaction safety around server-issued idempotency references and persisted payment intents; resolved ambiguous ledger outcomes through reconciliation, a background sweeper and classified connector responses.",
            "Implemented payment state machines for MTN, Syriatel and SEP integrations, including voucher workflows, and corrected SOAP request signing for accepted provider operations.",
            "Built bill-payment orchestration for biller catalogs, presentment, scheduled operations and reversal retries using Celery periodic tasks and Redis locks.",
            "Built merchant onboarding (KYB), QR and bill payments, agent escrow cash-out, maker-checker payment limits, and a loyalty ledger with earning rules, cashback, vouchers and fee waivers.",
            "Developed Flask and FastAPI services for Al Sharq Bank's Fintech Studio customer e-banking application and staff dashboard, secured with Keycloak and exposed through WSO2 API Manager.",
            "Added Keycloak-powered financial PIN, password recovery, lockout, trusted-device and role workflows, and maker-checker approvals for corporate and merchant operations.",
            "Integrated identity-verification start/status and approval webhooks, and added document-driven identity checks and staff review holds for mismatched customer data.",
            "Implemented staff RBAC, separate JWT audiences, append-only audit trails and correlation IDs; built bank deposit matching from statement lines with full or partial credits and an audit trail.",
            "Also worked on Odoo 19 development for Mawjud, a B2C e-commerce platform, and set up GitHub Actions deployment to staging and guarded production.",
        ],
    )
    role(pdf, "Backend Developer", "MadFox Solutions", "Aug 2024 – Nov 2025  ·  Full-time  ·  On-site, Syria")
    bullets(
        pdf,
        [
            "Built Flask microservices and REST APIs for banking web/mobile apps, serving customers, agents and operations teams; supported production debugging, data integrity and service-to-service integrations.",
            "Built APIs for JumlaTech's consumer, sales, delivery, and money-collection applications.",
        ],
    )
    role(
        pdf,
        "Software Engineer",
        "ARAMED (Arabian Medical Enterprises)",
        "Dec 2023 – Aug 2024  ·  Full-time  ·  Remote",
    )
    bullets(
        pdf,
        [
            "Developed and customized the company's Odoo 15 ERP across accounting, inventory, sales, and purchasing, and helped fix day-to-day ERP issues.",
        ],
    )

    heading(pdf, "Selected projects")
    role(pdf, "Wafra Pay", "rmz  ·  Digital wallet and banking integrations", "")
    bullets(
        pdf,
        [
            "End-to-end digital wallet flows connecting wallet provisioning, P2P/QR/bill payments, bank deposit matching and loyalty redemption with an Apache Fineract ledger.",
            "FastAPI wallet backend and a Flask connector to Apache Fineract covering agent cash-out and own-account bank withdrawals.",
            "Loyalty points module (earn/redeem ledger, dynamic rules, cashback, vouchers, fee waivers) and bank deposit matching from statement lines.",
        ],
    )
    role(pdf, "Al Sharq Bank Fintech Studio", "rmz  ·  E-banking platform", "")
    bullets(
        pdf,
        [
            "Customer e-banking and staff operations: bill presentment, mobile operator payments, reversals, customer security and corporate onboarding, with Keycloak and WSO2.",
            "Financial PIN, password recovery, lockout, trusted-device and role workflows, and maker-checker approval for dashboard changes.",
        ],
    )
    role(pdf, "Wafra KYC", "rmz  ·  Identity verification", "")
    bullets(
        pdf,
        [
            "Document OCR (including Arabic and Syrian ID), MRZ/barcode parsing, liveness and face matching, and configurable flow rules behind one API, plus start/status and approval webhooks.",
        ],
    )
    role(pdf, "Mawjud", "rmz  ·  Odoo 19, B2C e-commerce", "")
    bullets(
        pdf,
        ["Odoo 19 development, with GitHub Actions deployment to staging and guarded production."],
    )

    heading(pdf, "Skills")
    for label, text in [
        ("Backend", "Python, FastAPI, Flask, REST APIs, SQLAlchemy, Celery, Redis, PostgreSQL, microservices, modular monoliths"),
        ("Fintech APIs", "Apache Fineract, payment intents, idempotency, transaction lifecycles, payment state machines, reconciliation"),
        ("Async and reliability", "Celery periodic tasks, Redis locks, webhooks, Alembic, Pytest, Docker, Kubernetes, Git, GitHub Actions, production debugging"),
        ("Security and onboarding", "Keycloak, JWT, RBAC, OTP, KYB, audit logging, WSO2, SEP"),
        ("Also", "Odoo 15/17/19 custom modules"),
    ]:
        block(pdf, 5, f"{label}: {text}", "Inter", 10)

    heading(pdf, "Education")
    block(pdf, 5.5, "B.Sc. in Information Technology Engineering", "Inter", 11, "B")
    block(pdf, 5.2, "Damascus University, Syria  ·  2019 – 2024", "Inter", 10.5)

    heading(pdf, "Languages")
    block(pdf, 5.5, "Arabic — Native\nEnglish — B2, approaching C1", "Inter", 10.5)

    OUT.parent.mkdir(parents=True, exist_ok=True)
    pdf.output(str(OUT))
    print(OUT, OUT.stat().st_size)


if __name__ == "__main__":
    main()
