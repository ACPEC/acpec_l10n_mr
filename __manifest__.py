# -*- coding: utf-8 -*-
# Copyright 2021 ACPEC Sarl
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Plan Comptable Mauritanien',
    'author': 'ACPEC SARL',
    'version': '1.2',
    'category': 'Localization',
    'website': 'https://www.acpec-sarl.com/',
    'description': u"""
Ce module charge un modèle de plan de comptes général pour la Mauritanie.
Il offre un ensemble réduit de comptes et de taxes suffisant pour démarrer avec ODOO.
Créer une base Odoo vierge. Installer ce module et puis installer le module de la comptabilité ; et c'est tout.""",
    
    'depends': ['base', 'account',],
    'data': [
        'data/l10n_mr_chart_data.xml',
        'data/account_data.xml',
        'data/account_tax_data.xml',
        'data/account_chart_template_data.xml',
        ],

    'installable': True,
    'auto_install': False,
}
