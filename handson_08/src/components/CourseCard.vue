<script setup>
defineProps({
  name: { type: String, required: true },
  code: { type: String, required: true },
  credits: { type: Number, required: true }
});
</script>

<template>
  <div class="course-card">
    <div class="card-badge">{{ code }}</div>
    <h3 class="course-title">{{ name }}</h3>
    <div class="course-meta">
      <span class="meta-tag">{{ credits }} Credits</span>
    </div>
    <div class="card-actions">
      <slot></slot>
    </div>
  </div>
</template>

<style scoped>
.course-card {
  background: var(--card-bg);
  border: 1px solid var(--border-color);
  border-radius: 12px;
  padding: 24px;
  position: relative;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
  box-shadow: 0 1px 3px rgba(0,0,0,0.05);
}

.course-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 12px 20px rgba(0, 0, 0, 0.08);
}

.card-badge {
  position: absolute;
  top: 16px;
  right: 16px;
  background: #eff6ff;
  color: var(--primary-color);
  font-size: 0.75rem;
  font-weight: 700;
  padding: 4px 8px;
  border-radius: 6px;
  text-transform: uppercase;
}

.course-title {
  margin: 12px 0 8px 0;
  font-size: 1.25rem;
  font-weight: 600;
  color: var(--text-main);
  line-height: 1.4;
}

.course-meta {
  margin-bottom: 20px;
}

.meta-tag {
  background: #f1f5f9;
  color: var(--text-muted);
  font-size: 0.8rem;
  padding: 4px 8px;
  border-radius: 4px;
  font-weight: 500;
}

.card-actions {
  display: flex;
  gap: 10px;
}
</style>