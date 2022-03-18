from odoo import api, SUPERUSER_ID
from odoo.http import WebRequest

def _weblearns_pre_init_hook(cr):
    print("Hello there pre init hook method called.")
    # cr.execute("""update res_partner set mobile='1234567890' where mobile is null""");
    # print("pre init hoook done with sql query.....")
    # cr.commit()
    # env = api.Environment(cr, SUPERUSER_ID, {})
    # env['res.partner'].hello_hook()

def _weblearns_post_init_hook(cr, registry):
    print("Hello you just executed post init hook method.")
    # cr.execute("update res_partner set vat='1234567890' where vat=''");
    # cr.commit()
    # env = api.Environment(cr, SUPERUSER_ID, {})
    # env['res.partner'].hello_hook()

def _weblearns_uninstall_hook(cr, registry):
    print("Hello your module uninstalled from uninstall_hook.")
    # cr.execute("update res_partner set vat='' where vat='1234567890'")
    # cr.commit()
    # env = api.Environment(cr, SUPERUSER_ID, {})
    # env['res.partner'].hello_hook()

def _weblearns_post_load_hook():

    monkey_patch_set_handler = WebRequest.set_handler

    def set_handler(self, endpoint, arguments, auth):
        monkey_patch_set_handler(self, endpoint, arguments, auth)


    WebRequest.set_handler = set_handler

    monkey_page_init = WebRequest.__init__

    def __init__(self, httprequest):
        monkey_page_init(self, httprequest)
        self.weblearns = "This is call from set_handler method using monkey patch"
        print(self.weblearns)

    WebRequest.__init__ = __init__