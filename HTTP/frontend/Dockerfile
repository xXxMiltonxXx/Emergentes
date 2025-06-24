# --- Build Stage ---
FROM node:18-alpine AS build

WORKDIR /app

# Copia los archivos de configuración del paquete e instala dependencias
COPY package.json package-lock.json* ./
RUN npm install

# Copia el resto de los archivos de la aplicación
COPY . .

# Define la URL de la API como un argumento de compilación
ARG PUBLIC_API_URL
ENV PUBLIC_API_URL=${PUBLIC_API_URL}

# Construye la aplicación
RUN npm run build

# --- Production Stage ---
FROM node:18-alpine

WORKDIR /app

# Copia el servidor independiente desde la etapa de compilación
COPY --from=build /app/dist/server/entry.mjs /app/entry.mjs

# Expone el puerto
EXPOSE 8080

# Comando para iniciar el servidor
CMD ["node", "/app/entry.mjs"]