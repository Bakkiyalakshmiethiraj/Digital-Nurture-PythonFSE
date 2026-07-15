<script setup>
import { useRouter } from 'vue-router';
import { useEnrollmentStore } from '../stores/enrollment';

const router = useRouter();
const enrollmentStore = useEnrollmentStore();

// Mock metrics data to show application analytical depth
const trainingStats = [
  { label: 'Technical Modules', count: '12+', color: '#2563eb', bg: '#eff6ff' },
  { label: 'Coding Milestones', count: '45/50', color: '#10b981', bg: '#dcfce7' },
  { label: 'Placement Mock Exams', count: '04', color: '#f59e0b', bg: '#fef3c7' }
];

// Mock company timeline updates to instantly draw alignment focus
const placementTimeline = [
  { event: 'Initial Profile Screening', status: 'Completed', date: 'July 10, 2026', current: false },
  { event: 'Technical Assessment & Aptitude', status: 'In Progress', date: 'July 14, 2026', current: true },
  { event: 'Mock Panel Interview Round', status: 'Scheduled', date: 'July 18, 2026', current: false }
];
</script>

<template>
  <div class="home-grid">
    <section class="hero-banner">
      <div class="hero-text">
        <span class="badge-accent">Student Performance Portal</span>
        <h1>Next-Gen Academic & Placement Workspace</h1>
        <p>Track your technical learning curriculum, manage elective course modules, and monitor placement readiness indicators all within a unified reactive interface.</p>
        <div class="hero-cta">
          <button class="btn-primary" @click="router.push('/courses')">Explore Courses</button>
          <button class="btn-outline" @click="router.push('/announcements')">View Notice Board</button>
        </div>
      </div>
      <div class="hero-graphic">
        <div class="code-box">
          <div class="code-header">
            <span class="dot red"></span>
            <span class="dot yellow"></span>
            <span class="dot green"></span>
            <span class="code-title">AppStore.ts</span>
          </div>
          <pre class="code-content"><code><span class="keyword">import</span> { defineStore } <span class="keyword">from</span> <span class="string">'pinia'</span>;

<span class="keyword">export const</span> useAuth = defineStore(<span class="string">'user'</span>, () => {
  <span class="keyword">const</span> isReady = ref(<span class="keyword">true</span>);
  <span class="keyword">const</span> track = <span class="string">'Cognizant GenC'</span>;
  <span class="keyword">return</span> { isReady, track };
});</code></pre>
        </div>
      </div>
    </section>

    <section class="metrics-grid">
      <div v-for="(stat, idx) in trainingStats" :key="idx" class="stat-card" :style="{ borderLeftColor: stat.color }">
        <div class="stat-info">
          <span class="stat-label">{{ stat.label }}</span>
          <h3 class="stat-count" :style="{ color: stat.color }">{{ stat.count }}</h3>
        </div>
        <div class="stat-icon-bg" :style="{ backgroundColor: stat.bg, color: stat.color }">📊</div>
      </div>
    </section>

    <div class="dashboard-columns">
      <div class="content-panel">
        <h3>Quick Access Hub</h3>
        <p class="panel-desc">Direct links to active development tasks and modules.</p>
        
        <div class="quick-links">
          <div class="link-item" @click="router.push('/profile')">
            <div class="link-icon">👤</div>
            <div class="link-details">
              <h4>Student Profile Matrix</h4>
              <p>Review registered credit calculations and drops.</p>
            </div>
            <span class="arrow">→</span>
          </div>

          <div class="link-item" @click="router.push('/courses')">
            <div class="link-icon">📚</div>
            <div class="link-details">
              <h4>Module Frameworks</h4>
              <p>Quickly enroll in reactive system architectural layers.</p>
            </div>
            <span class="arrow">→</span>
          </div>
        </div>
      </div>

      <div class="content-panel">
        <h3>Placement Roadmap Status</h3>
        <p class="panel-desc">Real-time status updates mapping to active institutional training targets.</p>
        
        <div class="timeline">
          <div v-for="(item, index) in placementTimeline" :key="index" :class="['timeline-item', { active: item.current }]">
            <div class="timeline-marker"></div>
            <div class="timeline-body">
              <div class="timeline-meta">
                <span class="timeline-event">{{ item.event }}</span>
                <span :class="['status-pill', item.status.toLowerCase().replace(' ', '-')]">{{ item.status }}</span>
              </div>
              <span class="timeline-date">{{ item.date }}</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.home-grid {
  display: flex;
  flex-direction: column;
  gap: 32px;
}

/* Hero Section Styles */
.hero-banner {
  background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
  border-radius: 16px;
  padding: 48px;
  color: white;
  display: grid;
  grid-template-columns: 1.2fr 0.8fr;
  align-items: center;
  gap: 40px;
  box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.1);
}

@media (max-width: 968px) {
  .hero-banner { grid-template-columns: 1fr; padding: 32px; }
  .hero-graphic { display: none; }
}

.badge-accent {
  background: rgba(37, 99, 235, 0.2);
  color: #60a5fa;
  border: 1px solid rgba(37, 99, 235, 0.4);
  padding: 6px 12px;
  border-radius: 20px;
  font-size: 0.8rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  display: inline-block;
  margin-bottom: 16px;
}

.hero-text h1 {
  font-size: 2.5rem;
  margin: 0 0 16px 0;
  font-weight: 700;
  letter-spacing: -0.5px;
  line-height: 1.2;
}

.hero-text p {
  color: #94a3b8;
  font-size: 1.1rem;
  line-height: 1.6;
  margin: 0 0 32px 0;
  max-width: 600px;
}

.hero-cta {
  display: flex;
  gap: 16px;
}

button {
  padding: 12px 24px;
  border-radius: 8px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s;
  font-size: 0.95rem;
}

.btn-primary { background: var(--primary-color); color: white; border: none; }
.btn-primary:hover { background: var(--primary-hover); transform: translateY(-1px); }

.btn-outline { background: transparent; color: white; border: 1px solid #475569; }
.btn-outline:hover { background: rgba(255, 255, 255, 0.05); border-color: #64748b; }

/* CSS Graphics Simulation */
.code-box {
  background: #090d16;
  border: 1px solid #1e293b;
  border-radius: 10px;
  font-family: 'Fira Code', monospace;
  overflow: hidden;
  box-shadow: 0 20px 25px -5px rgba(0,0,0,0.3);
}
.code-header {
  background: #111827;
  padding: 10px 16px;
  display: flex;
  align-items: center;
  gap: 6px;
  border-bottom: 1px solid #1e293b;
}
.dot { width: 10px; height: 10px; border-radius: 50%; display: inline-block; }
.red { background: #ef4444; } .yellow { background: #f59e0b; } .green { background: #10b981; }
.code-title { color: #64748b; font-size: 0.75rem; margin-left: 10px; }
.code-content { margin: 0; padding: 20px; font-size: 0.85rem; color: #cbd5e1; overflow-x: auto;}
.keyword { color: #f43f5e; } .string { color: #10b981; }

/* Metrics Section */
.metrics-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 24px;
}

.stat-card {
  background: var(--card-bg);
  border: 1px solid var(--border-color);
  border-left: 4px solid #cbd5e1;
  border-radius: 12px;
  padding: 24px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  box-shadow: 0 1px 3px rgba(0,0,0,0.02);
}

.stat-label { color: var(--text-muted); font-size: 0.9rem; font-weight: 500; }
.stat-count { font-size: 1.75rem; margin: 6px 0 0 0; font-weight: 700; }
.stat-icon-bg { width: 48px; height: 48px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.25rem; }

/* Dashboard Content Grid splits */
.dashboard-columns {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 32px;
}
@media (max-width: 768px) { .dashboard-columns { grid-template-columns: 1fr; } }

.content-panel {
  background: var(--card-bg);
  border: 1px solid var(--border-color);
  border-radius: 12px;
  padding: 28px;
}
.content-panel h3 { margin: 0; font-size: 1.25rem; }
.panel-desc { margin: 4px 0 24px 0; color: var(--text-muted); font-size: 0.9rem; }

/* Quick Link Navigation Styles */
.quick-links { display: flex; flex-direction: column; gap: 16px; }
.link-item {
  display: flex;
  align-items: center;
  padding: 16px;
  border: 1px solid var(--border-color);
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.2s;
}
.link-item:hover { background: #f8fafc; border-color: var(--primary-color); }
.link-icon { font-size: 1.5rem; margin-right: 16px; }
.link-details { flex: 1; }
.link-details h4 { margin: 0 0 4px 0; font-size: 0.95rem; }
.link-details p { margin: 0; color: var(--text-muted); font-size: 0.85rem; }
.arrow { color: var(--text-muted); font-weight: bold; font-size: 1.1rem; }

/* Roadmap Timeline Framework UI */
.timeline { display: flex; flex-direction: column; gap: 20px; position: relative; padding-left: 20px; }
.timeline::before { content: ''; position: absolute; left: 4px; top: 8px; bottom: 8px; width: 2px; background: var(--border-color); }
.timeline-item { position: relative; }
.timeline-marker { position: absolute; left: -20px; top: 6px; width: 10px; height: 10px; border-radius: 50%; background: #cbd5e1; border: 2px solid white; transition: all 0.3s; }
.timeline-item.active .timeline-marker { background: var(--primary-color); box-shadow: 0 0 0 4px rgba(37, 99, 235, 0.2); }
.timeline-body { display: flex; flex-direction: column; gap: 4px; background: #f8fafc; padding: 12px 16px; border-radius: 8px; }
.timeline-meta { display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 8px; }
.timeline-event { font-weight: 600; font-size: 0.95rem; }
.timeline-date { font-size: 0.8rem; color: var(--text-muted); }
.status-pill { font-size: 0.7rem; padding: 2px 8px; border-radius: 12px; font-weight: 700; text-transform: uppercase; }
.status-pill.completed { background: #dcfce7; color: #16a34a; }
.status-pill.in-progress { background: #eff6ff; color: #2563eb; }
.status-pill.scheduled { background: #f1f5f9; color: #475569; }
</style>