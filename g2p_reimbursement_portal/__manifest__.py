{
    "name": "G2P Reimbursement Portal",
    "category": "G2P",
    "version": "17.0.1.0.0",
    "sequence": 1,
    "author": "OpenG2P",
    "website": "https://openg2p.org",
    "license": "Other OSI approved licence",
    "development_status": "Alpha",
    "depends": ["g2p_program_reimbursement", "g2p_agent_portal_base", "g2p_program_cycleless"],
    "data": [
        "data/g2p_reimbursement_portal_form_data.xml",
        "views/g2p_portal_reimbursement.xml",
        "views/g2p_portal_form_template.xml",
        "views/g2p_portal_form_submitted.xml",
        "views/g2p_portal_dashboard.xml",
        "views/home.xml",
        "views/login.xml",
        "views/profile.xml",
        "views/website_page.xml",
    ],
    "assets": {
        "website.assets_wysiwyg": [
            "g2p_reimbursement_portal/static/src/js/reim_form_editor.js",
        ],
    },
    "demo": [],
    "images": [],
    "application": True,
    "installable": True,
    "auto_install": False,
}
