from datetime import datetime, timedelta

from odoo.tests.common import TransactionCase


class TestG2PEntitlement(TransactionCase):
    def setUp(self):
        super().setUp()
        self.program = self.env["g2p.program"].create({"name": "Test Program"})
        self.partner = self.env["res.partner"].create({"name": "Test Partner"})
        self.cycle = self.env["g2p.cycle"].create(
            {
                "name": "Test Cycle",
                "program_id": self.program.id,
                "start_date": datetime.now(),
                "end_date": datetime.now() + timedelta(days=30),
            }
        )
        self.entitlement = self.env["g2p.entitlement"].create(
            {
                "program_id": self.program.id,
                "partner_id": self.partner.id,
                "cycle_id": self.cycle.id,
                "state": "draft",
                "initial_amount": 100,
            }
        )

    def test_compute_show_voucher_buttons(self):
        self.entitlement.state = "approved"
        self.entitlement._compute_show_voucher_buttons()
        self.assertTrue(self.entitlement.show_generate_voucher_button)

    def test_generate_vouchers_action(self):
        self.entitlement.state = "approved"
        action = self.entitlement.generate_vouchers_action()
        self.assertTrue(action)

    def test_print_voucher_action(self):
        # Assuming voucher_document_id is set
        self.entitlement.voucher_document_id = self.env["storage.file"].create(
            {"name": "Test Voucher", "backend_id": 1}
        )
        action = self.entitlement.print_voucher_action()
        self.assertEqual(action["type"], "ir.actions.act_url")
        self.assertIn("Voucher", action["name"])
        self.assertEqual(action["target"], "new")
        self.assertIn(self.entitlement.voucher_document_id.url, action["url"])
