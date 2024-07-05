const { createApp, ref } = Vue;

const app = createApp({
  setup() {
    const cart = ref(0);
    const onSale = ref(true);
    const inStock = ref(true);
    const inventory = ref(100);
    const product = ref("Socks");
    const image = ref("./assets/images/socks_green.jpg");
    const details = ref(["50% cotton", "30% wool", "20% polyester"]);
    const url = ref("https://www.linkedin.com/in/ricardoandreh/");
    const sizes = ref(["S", "M", "L", "XL"]);
    const variants = ref([
      { id: 2234, color: "green", image: "./assets/images/socks_green.jpg" }, 
      { id: 2235, color: "blue", image: "./assets/images/socks_blue.jpg" }, 
    ]);

    const addToCart = () => cart.value++;
    const removeFromCart = () => cart.value > 0 && cart.value--;
    const updateImage = (variantImage) => image.value = variantImage;

    return {
      product, image, url, 
      inStock, inventory, onSale, 
      details, variants, sizes, 
      cart, addToCart, updateImage, 
      removeFromCart, 
    }
  }
});
