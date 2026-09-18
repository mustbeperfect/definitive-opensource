
<template>
  <div class="border border-gray-200 p-2">
    <h2>{{ app.name }}</h2>
    <p>{{ app.description }}</p>

    <div class="">
      <span class="">{{ app.stars.toLocaleString() }}</span>
      <span class="">Language: {{ app.language }}</span>
      <span class="">License: {{ app.license }}</span>
      <span class="">Category: {{ app.category }}</span>
    </div>

    <div class="">
      <a :href="app.repo_url" target="_blank" rel="noopener noreferrer">GitHub Repo</a>
      <a v-if="app.homepage_url" :href="app.homepage_url" target="_blank" rel="noopener noreferrer"
        >Homepage</a
      >
    </div>
  </div>
</template>

<script setup lang="ts">
import type { Application } from '@/types'

defineProps<{
  app: Application
}>()
</script>

<style scoped>

</style>
