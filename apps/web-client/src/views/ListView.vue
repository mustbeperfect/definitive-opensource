
<template>
  <div class="">

    <div v-if="loading" class="status">Loading applications...</div>

    <div v-else-if="error" class="text-red-500">
      {{ error }}
    </div>

    <div v-else class="flex flex-col gap-2 p-5">
      <ApplicationCard v-for="app in applications" :key="app.repo_url" :app="app" />
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import ApplicationCard from '../components/ApplicationCard.vue'
import type { Application } from '@/types'

const applications = ref<Application[]>([])
const loading = ref(true)
const error = ref<string | null>(null)

onMounted(async () => {
  try {
    const response = await fetch(
      'https://raw.githubusercontent.com/mustbeperfect/definitive-opensource/refs/heads/main/core/data/dynamic/applications_generated.json',
    )

    if (!response.ok) {
      throw new Error(`Error fetching data: ${response.statusText}`)
    }

    const data = await response.json()

    applications.value = data.applications
  } catch (e) {
    error.value = e instanceof Error ? e.message : 'An unknown error occurred'
    console.error(e)
  } finally {
    loading.value = false
  }
})
</script>

<style scoped></style>
