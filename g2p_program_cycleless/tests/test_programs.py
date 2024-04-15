from datetime import datetime, timedelta

from odoo.tests import common


class TestG2PPrograms(common.TransactionCase):
    def setUp(self):
        super().setUp()

        # Create a cycle-based and a cycleless program
        self.cycle_based_program = self.env["g2p.program"].create({"name": "Cycle-Based Program"})
        self.cycleless_program = self.env["g2p.program"].create(
            {"name": "Cycleless Program", "is_cycleless": True}
        )
        self.program = self.env["g2p.program"].create({"name": "Test Program"})
        self.program = self.env["res.partner"].create({"name": "Test Program"})

    def test_default_active_cycle_cycle_based(self):
        # Create two cycles with different states
        cycle1 = self.cycle_based_program.cycle_ids.create(
            {
                "name": "Test Cycle1",
                "program_id": self.cycle_based_program.id,
                "start_date": datetime.now(),
                "end_date": datetime.now() + timedelta(days=30),
                "state": "approved",
            }
        )
        self.cycle_based_program.cycle_ids.create(
            {
                "name": "Test Cycle2",
                "program_id": self.cycle_based_program.id,
                "start_date": datetime.now(),
                "end_date": datetime.now() + timedelta(days=30),
                "state": "to_approve",
            }
        )

        # Assert that the most recently approved cycle is the default active cycle
        self.assertEqual(self.cycle_based_program.default_active_cycle, cycle1)

    # TODO : revisit the following test cases
    # def test_default_active_cycle_cycleless(self):
    #     # Create a cycle for the cycleless program
    #     self.cycleless_program.create_new_cycle()

    #     # Assert that the cycle is not assigned as the default active cycle (should be None)
    #     self.assertFalse(self.cycleless_program.default_active_cycle)

    # def test_show_cycleless_fields_cycle_based(self):
    #     # Assert that cycleless fields are not shown for a cycle-based program
    #     self.assertFalse(self.cycle_based_program.show_prepare_payments_button)
    #     self.assertFalse(self.cycle_based_program.show_send_payments_button)

    # def test_show_cycleless_fields_cycleless_active_with_payment_manager(self):
    #     # Assign a payment manager to the cycleless program
    #     self.cycleless_program.write(
    #         {
    #             "manager_id": self.env["g2p.program.payment.manager.phee"].create(
    #                 {
    #                     "program_id": self.program.id,
    #                     "name": "Manager",
    #                 }
    #             ).id
    #         }
    #     )

    #     # Assert that cycleless payment buttons are displayed
    #     self.assertTrue(self.cycleless_program.show_prepare_payments_button)
    #     self.assertTrue(self.cycleless_program.show_send_payments_button)

    # def test_show_cycleless_fields_cycleless_inactive(self):
    #     # Change the program state to inactive
    #     self.cycleless_program.state = "ended"

    #     # Assert that cycleless payment buttons are not displayed
    #     self.assertFalse(self.cycleless_program.show_prepare_payments_button)
    #     self.assertFalse(self.cycleless_program.show_send_payments_button)

    # def test_open_entitlements_form(self):
    #     # Create a cycle for the program
    #     cycle = self.cycle_based_program.cycle_ids.create({
    #             "name": "Test Cycle",
    #             "program_id": self.cycle_based_program.id,
    #             "start_date": datetime.now(),
    #             "end_date": datetime.now() + timedelta(days=30),})

    #     # Call open_entitlements_form and assert that it calls the correct method on the cycle
    #     with mock.patch(
    #         "odoo.addons.g2p_program_cycleless.models.programs.G2PPrograms.open_entitlements_form"
    #     ) as mock_open_entitlements:
    #         self.cycle_based_program.open_entitlements_form()
    #         mock_open_entitlements.assert_called_once()

    # def test_prepare_payments_cycleless(self):
    #     # Create a cycle for the cycleless program
    #     cycle = self.cycleless_program.create_new_cycle()

    #     # Call prepare_payments_cycleless and assert that it calls the correct method on the cycle
    #     with mock.patch.object(cycle, "prepare_payment") as mock_prepare_payment:
    #         self.cycleless_program.prepare_payments_cycleless()
    #         mock_prepare_payment.assert_called_once()

    # def test_send_payments_cycleless(self):
    #     # Create a cycle for the cycleless program
    #     cycle = self.cycleless_program.create_new_cycle()

    #     # Call send_payments_cycleless and assert that it calls the correct method on the cycle
    #     with mock.patch.object(cycle, "send_payment") as mock_send_payment:
    #         self.cycleless_program.send_payments_cycleless()
    #         mock_send_payment.assert_called_once()
