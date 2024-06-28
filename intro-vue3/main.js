const { createApp, ref } = Vue;

const app = createApp({
  setup() {
    const onSale = ref(true);
    const inStock = ref(true);
    const inventory = ref(100);
    const product = ref("Socks");
    const image = ref("./assets/images/socks_green.jpg");
    const url = ref("https://www.linkedin.com/in/ricardoandreh/");
    
    return {
      product, image, 
      url, inStock, 
      inventory, onSale, 
    }
  }
});
