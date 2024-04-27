const { createApp, ref } = Vue;

const app = createApp({
  setup() {
    const product = ref("Socks");
    const image = ref("./assets/images/socks_green.jpg");
    const url = ref("https://www.linkedin.com/in/ricardoandreh/");
    
    return {
      product, image, url
    }
  }
});
