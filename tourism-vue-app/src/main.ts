import { createApp } from "vue";
import App from "./App.vue";
import "./assets/tailwind.css";
import router from "./router";
import "boxicons/css/boxicons.min.css";
import i18n from "./utils/i18n";

type SupportedLanguages = "es" | "en";

const savedLanguage = localStorage.getItem("selectedLanguage") as SupportedLanguages | null;

if (savedLanguage && (savedLanguage === "es" || savedLanguage === "en")) {
  i18n.global.locale = savedLanguage;
} else {
  localStorage.setItem("selectedLanguage", i18n.global.locale);
}

createApp(App).use(router).use(i18n).mount("#app");
