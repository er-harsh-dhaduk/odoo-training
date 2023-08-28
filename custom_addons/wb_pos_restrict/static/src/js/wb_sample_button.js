/** @odoo-module **/

import { PosGlobalState } from 'point_of_sale.models';
import Registries from 'point_of_sale.Registries';


const PosButtonRestrict = (PosGlobalState) => class PosButtonRestrict extends PosGlobalState{

    async _processData(loadedData){
        await super._processData(...arguments);
        this.visible_backspace_btn = loadedData['visible_backspace_btn']
    }
}

Registries.Model.extend(PosGlobalState, PosButtonRestrict);