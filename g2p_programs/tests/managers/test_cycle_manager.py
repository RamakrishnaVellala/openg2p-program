# from odoo.tests import common
# from odoo.exceptions import UserError

# class TestCycleManagers(common.TransactionCase):
#     def setUp(self):
#         super(TestCycleManagers, self).setUp()
#         self.program = self.env["g2p.program"].create({"name": "Test Program"})
#         self.cycle_manager = self.env["g2p.cycle.manager"].create({
#             "name": "Test Cycle Manager",
#             "program_id": self.program.id,
#         })

#     def test_base_cycle_manager_abstract_methods(self):
#         with self.assertRaises(NotImplementedError):
#             self.cycle_manager.check_eligibility(None)
#         with self.assertRaises(NotImplementedError):
#             self.cycle_manager.prepare_entitlements(None)
#         with self.assertRaises(NotImplementedError):
#             self.cycle_manager.issue_payments(None)
#         with self.assertRaises(NotImplementedError):
#             self.cycle_manager.validate_entitlements(None)
#         with self.assertRaises(NotImplementedError):
#             self.cycle_manager.new_cycle(None, None, None)
#         with self.assertRaises(NotImplementedError):
#             self.cycle_manager.mark_distributed(None)
#         with self.assertRaises(NotImplementedError):
#             self.cycle_manager.mark_ended(None)
#         with self.assertRaises(NotImplementedError):
#             self.cycle_manager.mark_cancelled(None)
#         with self.assertRaises(NotImplementedError):
#             self.cycle_manager.add_beneficiaries(None, None)
#         with self.assertRaises(NotImplementedError):
#             self.cycle_manager.on_start_date_change(None)
#         with self.assertRaises(NotImplementedError):
#             self.cycle_manager.approve_cycle(None)

#     def test_default_cycle_manager_methods(self):
#         default_cycle_manager = self.env["g2p.cycle.manager.default"].create({
#             "name": "Default Cycle Manager",
#             "program_id": self.program.id,
#         })
#         cycle = self.env["g2p.cycle"].create({
#             "name": "Test Cycle",
#             "program_id": self.program.id,
#             "state": "draft",
#         })

#         # Test check_eligibility
#         action = default_cycle_manager.check_eligibility(cycle)
#         self.assertTrue(action["type"], "ir.actions.client")

#         # Test prepare_entitlements
#         with self.assertRaises(UserError):
#             default_cycle_manager.prepare_entitlements(cycle)

#         # Test mark_distributed, mark_ended, mark_cancelled
#         default_cycle_manager.mark_distributed(cycle)
#         self.assertEqual(cycle.state, "distributed")
#         default_cycle_manager.mark_ended(cycle)
#         self.assertEqual(cycle.state, "ended")
#         default_cycle_manager.mark_cancelled(cycle)
#         self.assertEqual(cycle.state, "cancelled")

#         # Test new_cycle
#         new_cycle = default_cycle_manager.new_cycle("New Cycle", fields.Date.today(), 1)
#         self.assertEqual(new_cycle.name, "New Cycle")
#         self.assertEqual(new_cycle.state, "draft")
#         self.assertEqual(new_cycle.sequence, 1)

#         # Test copy_beneficiaries_from_program
#         beneficiaries_count = len(default_cycle_manager.copy_beneficiaries_from_program(cycle))
#         self.assertEqual(beneficiaries_count, 0)

#         # Test add_beneficiaries
#         beneficiaries = [self.env["res.partner"].create({"name": "Beneficiary"})]
#         action = default_cycle_manager.add_beneficiaries(cycle, beneficiaries)
#         self.assertTrue(action["type"], "ir.actions.client")

#         # Test _compute_interval
#         default_cycle_manager.cycle_duration = 10
#         default_cycle_manager._compute_interval()
#         self.assertEqual(default_cycle_manager.interval, 10)
