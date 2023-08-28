odoo.define("wb_pos.WBSampleButton", function(require){
"use strict";

    const PosComponent = require("point_of_sale.PosComponent");
    const ProductScreen = require("point_of_sale.ProductScreen");
    const Registries = require("point_of_sale.Registries");
    const { useListener } = require("@web/core/utils/hooks");
    const core  = require("web.core");
    var _t = core._t;

    class WBSampleButton extends PosComponent {

        setup(){
            super.setup();
            useListener("click", this.wb_sample_button_click);
        }

        async wb_sample_button_click(){

            var multi_lang = await this.rpc({
                route:"/pos/rpc/example",
                params:{},
            })


            console.log("language ---> ", multi_lang);

            var multi_lang_list = [];

            multi_lang.forEach(function(value){
                   multi_lang_list.push({"id": value.id,
                   "label":value.name,
                   "item": value});
            });

            console.log(multi_lang_list);

            var {confirmed, payload: selectedOption} = await this.showPopup("SelectionPopup", {
                title: "Active Languages!",
                list: multi_lang_list
            })

            console.log(confirmed, selectedOption);

//            var result = await this.rpc({
//                'model':"res.lang",
//                "method":"search_read",
//                "args":[[], ['id','name','code']],
//            });

//            var result = await this.rpc({
//                route: '/pos/rpc/example',
//                params: {}
//            })
//
//            console.log(result);
//
//            result.forEach(function(value){
//                console.log("Record---> ",value);
//            })



//            this.showPopup("ErrorPopup", {
//                title: _t("Error Message"),
//                body: this.env._t("The simple Error message screen."),
//            });
//
//            var { confirmed }= await this.showPopup("ConfirmPopup",{
//                title: _t("Confirm Popup"),
//                body: _t("ARe you sure want to continue?"),
//                confirmText: _t("Yes"),
//                cancelText: _t("No")
//            });
//            if (confirmed){
//                console.log("clicked to Yes button");
//            }else{
//                console.log("clicked to No button");
//            }
//            console.log("confirm button", confirmed)
//
//            this.showPopup("OfflineErrorPopup",{
//                title: _t("Odoo Error"),
//                body: this.env._t("Hey this is test popup screen, don't take seriously!")
//            })
//
//            var { confirmed, payload: selectedOption } = await this.showPopup("SelectionPopup",{
//                title: this.env._t("Are you a good JS developer ?"),
//                list: [{'id':0,'label': _t("Yes"),'item':"You pressed Yes"},
//                        {'id':1,'label':_t("No"),'item':"You pressed No"},
//                        {'id':2,'label': _t("Not Sure"),'item':"You pressed Not Sure!!!!"}]
//            });
//
//            console.log(confirmed);
//            console.log(selectedOption);
//            const info = await this.env.pos.getClosePosInfo();
//            this.showPopup("ClosePosPopup",{
//                info: info,
//                keepBehind:true
//            })

            console.log("Hello this is button click event pressed........");
        }

    }

    WBSampleButton.template = "WBSampleButton";
    ProductScreen.addControlButton({
        component: WBSampleButton,
        position: ["before", "OrderlineCustomerNoteButton"],
    });

    Registries.Component.add(WBSampleButton);

    return WBSampleButton;

});