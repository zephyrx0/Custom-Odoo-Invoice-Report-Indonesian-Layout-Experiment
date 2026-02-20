FROM odoo:18.0
# Kalau lu punya custom addons, uncomment baris di bawah ini
COPY ./custom_addons /mnt/extra-addons
USER odoo