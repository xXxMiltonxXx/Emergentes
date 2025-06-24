import { defineConfig } from 'astro/config';
import preact from '@astrojs/preact';

// https://astro.build/config
export default defineConfig({
  integrations: [preact()],
  server: {
    host: '0.0.0.0',
    port: 8080
  },
  output: 'server'
});