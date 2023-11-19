/** @odoo-module **/

import { ListController } from "@web/views/list/list_controller";
import { patch } from "@web/core/utils/patch";
import { useService } from "@web/core/utils/hooks";

patch(ListController.prototype, "wb_student_weblearns",{

    setup(){
        this._super.apply();
        this.action = useService("action");
    },

    wbButtonClickeEvent(){
        this.action.doAction({
            type:"ir.actions.act_window",
            name:"Mass School Profile Update",
            view_mode:"form",
            target:"new",
            res_model:"set.default.school.wiz",
            views:[[false, "form"]],
            context:'{"default_student_ids":['+ this.model.root.selection.map((datapoint) => datapoint.resId)+']}'
        })
    }
});