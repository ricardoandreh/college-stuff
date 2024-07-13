const { inject } = Vue;

app.component("product-display", {
  props: {
    premium: {
      type: Boolean,
      required: true,
    },
    details: {
      type: Array,
      required: true,
    },
  },
  emits: ["add-to-cart", "remove-from-cart"],
  setup(props) {
    const onSale = ref(true);
    const inventory = ref(11);
    const product = ref("Socks");
    const selectedVariant = ref(0);
    const brand = ref("Vue Mastery");
    const url = ref("https://www.linkedin.com/in/ricardoandreh/");
    const variants = ref([
      {
        id: 2234,
        color: "green",
        image: "./assets/images/socks_green.jpg",
        quantity: 50,
      },
      {
        id: 2235,
        color: "blue",
        image: "./assets/images/socks_blue.jpg",
        quantity: 0,
      },
    ]);

    const title = computed(() => brand.value + " " + product.value);
    const image = computed(() => variants.value[selectedVariant.value].image);
    const inStock = computed(
      () => variants.value[selectedVariant.value].quantity
    );
    const shipping = computed(() => (props.premium ? "Free" : 2.99));

    const updateVariant = (index) => (selectedVariant.value = index);

    const cart = inject("cart");

    return {
      onSale, product, selectedVariant, 
      brand, url, variants, title, image, cart, 
      inStock, shipping, inventory, updateVariant, 
    };
  },
  template: `
    <div class="product-display">
      <div class="product-container">
        <div class="product-image">
          <img
            :class="[ !inStock ? 'out-of-stock-img' : '' ]"
            :src="image"
          />
        </div>
        <div class="product-info">
          <h1>{{ title }}</h1>

          <p v-if="inventory > 10">Em Estoque</p>
          <p v-else-if="inventory <= 10 && inventory > 0">
            Quase esgotado!
          </p>
          <p v-else>Fora de Estoque</p>
          <p>Shipping: {{ shipping }}</p>

          <p v-show="onSale">{{ title }} is on sale.</p>

          <ul v-for="detail, index in details" :key="index">
            <li>{{ detail }}</li>
          </ul>

          <div
            v-for="variant, index in variants"
            :key="variant.id"
            @mouseover="updateVariant(index)"
            class="color-circle"
            :style="{ backgroundColor: variant.color }"
          ></div>

          <button
            class="button"
            :class="{ disabledButton: !inStock }"
            :disabled="!inStock"
            @click="$emit('add-to-cart', variants[selectedVariant])"
          >
            Add to Cart
          </button>
          <button
            class="button"
            :class="{ disabledButton: cart <= 0 }"
            :disabled="cart <= 0"
            @click="$emit('remove-from-cart')"
          >
            Remove Item
          </button>
          <br />
          <a :href="url" target="_blank">Made by Ricardo André</a>
        </div>
      </div>
    </div>`,
});
