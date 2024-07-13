const { createApp, ref, computed } = Vue;

const app = createApp({
  setup() {
    const cart = ref(0);
    const onSale = ref(true);
    const inventory = ref(100);
    const product = ref("Socks");
    const selectedVariant = ref(0);
    const brand = ref("Vue Mastery");
    const details = ref(["50% cotton", "30% wool", "20% polyester"]);
    const url = ref("https://www.linkedin.com/in/ricardoandreh/");
    const sizes = ref(["S", "M", "L", "XL"]);
    const variants = ref([
      { id: 2234, color: "green", image: "./assets/images/socks_green.jpg", quantity: 50 }, 
      { id: 2235, color: "blue", image: "./assets/images/socks_blue.jpg", quantity: 0 }, 
    ]);

    const title = computed(() => brand.value + ' ' + product.value);
    const image = computed(() => variants.value[selectedVariant.value].image);
    const inStock = computed(() => variants.value[selectedVariant.value].quantity);
    
    const addToCart = () => cart.value++;
    const removeFromCart = () => cart.value > 0 && cart.value--;
    const updateImage = (variantImage) => image.value = variantImage;
    const updateVariant = (index) => selectedVariant.value = index;
    
    return {
      product, image, url, 
      inStock, inventory, onSale, 
      details, variants, sizes, 
      cart, addToCart, updateImage, 
      removeFromCart, brand, title, 
      selectedVariant, updateVariant, 
    }
  }
});
