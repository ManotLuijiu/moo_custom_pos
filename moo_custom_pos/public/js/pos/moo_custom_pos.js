frappe.provide('moo_custom_pos');

moo_custom_pos.MooCustomPOS = class MooCustomPOS {
    constructor(wrapper) {
        this.wrapper = wrapper;
        this.init_component();
    }

    init_component() {
        this.prepare_dom();
        this.setup_vue();
    }

    prepare_dom() {
        this.wrapper.innerHTML = `
            <div id="moo-custom-pos">
                <div id="pos-component"></div>
            </div>
        `
    }

    setup_vue() {
        // Initialize Vue app
        const app = Vue.createApp({
            template: `
                <div class="custom-pos-container">
                    <pos-header></pos-header>
                    <pos-items></pos-items>
                    <pos-cart></pos-cart>
                </div>
            `
        })

        // Register components
        app.component('pos-header', this.get_header_component());
        app.component('pos-items', this.get_items_component());
        app.component('pos-cart', this.get_cart_component());

        // Mount the app
        app.mount('#pos-component');
    }

    get_header_component() {
        return {
            template: `
                <div class="pos-header">
                    <!-- Header content -->
                </div>
            `
        }
    }

    get_items_component() {
        return {
            template: `
                <div class="pos-items">
                    <!-- Item grid with unit selection -->
                    <div v-for="item in items" :key="item.item_code">
                        <div class="item-card">
                            <select v-model="item.unit" @change="updatePrice(item)">
                                <option value="piece">Piece</option>
                                <option value="dozen">Dozen</option>
                            </select>
                            <div class="price">{{ formatPrice(item.price) }}</div>
                        </div>
                    </div>
                </div>
            `,
            data() {
                return {
                    items: [],
                    unitConversions: {
                        dozen: 12,
                        piece: 1,
                    }
                }
            },
            methods: {
                updatePrice(item) {
                    const conversion = this.unitConversions[item.unit];
                    item.price = item.base_price * conversion;
                }
            }
        }
    }

    get_cart_component() {
        return {
            template: `
                <div class="pos-cart">
                    <!-- Cart Items -->
                </div>
            `
        }
    }
}