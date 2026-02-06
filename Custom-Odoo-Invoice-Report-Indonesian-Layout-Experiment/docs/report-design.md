# Report Design

The report is designed with the principle of not modifying Odoo's invoice logic, but only adjusting the presentation layer (QWeb report).

Design approach:

- Extend the existing invoice report template using QWeb inheritance
- Add a function to convert numeric amount into Indonesian words (terbilang)
- Add additional layout sections at the bottom for:
  - Signature
  - Company stamp
  - Terbilang text
- Keep compatibility with standard Odoo invoice data model

This ensures the customization remains lightweight and focused only on the visual and document convention aspect.
