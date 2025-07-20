import { createApp } from 'vue'

const App = {
  data() {
    return { topic: '', result: '' }
  },
  methods: {
    async run() {
      const resp = await fetch(`http://localhost:8000/run?topic=${encodeURIComponent(this.topic)}`)
      const data = await resp.json()
      this.result = data.result
    }
  },
  template: `
    <div>
      <h1>CrewAI Vue Template</h1>
      <input v-model="topic" placeholder="Enter topic" />
      <button @click="run">Run</button>
      <pre>{{ result }}</pre>
    </div>
  `
}

createApp(App).mount('#app')
