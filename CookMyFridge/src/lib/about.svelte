<script lang="ts">
    import { fade, fly } from 'svelte/transition';
  </script>
  
  <style>
    .parallax {
      background-attachment: fixed;
      background-position: center;
      background-repeat: no-repeat;
      background-size: cover;
    }
  </style>
  
  <div class="relative">
    <section class="h-screen flex flex-col justify-center items-center bg-gray-200 space-y-5">
      <div transition:fade={{ delay: 300, duration: 600 }} class="text-center">
        <img src="logo.png" class="max-w-xs rounded-full shadow-lg" alt="CookMyFridge Logo">
        <p class="text-xl font-bold mt-5">Welcome to CookMyFridge</p>
        <p class="text-md text-gray-600">The ultimate kitchen companion for creative cooking!</p>
      </div>
    </section>
  
    <section class="h-screen flex justify-center items-center bg-gray-200">
        <div class="flex items-center space-x-10">
          <div transition:fly={{ x: -200, delay: 500 }} class="flex justify-center">
            <img src="camera.png" alt="Dynamic Content" class="max-w-xs rounded-lg shadow-lg">
          </div>
          <div transition:fly={{ x: 200, delay: 500 }} class="p-10 text-white rounded-lg bg-black bg-opacity-50 shadow-2xl">
            <p>How it works: snap a picture of your fridge's content.</p>
            <p class="text-sm mt-4">Just open the app, take a photo, and let our AI do the rest.</p>
          </div>
        </div>
      </section>

      <section class="h-screen flex justify-center items-center bg-gray-100">
        <div class="flex items-center space-x-10 bg-cover bg-center rounded-lg shadow-2xl" style="background-image: url('detection.png');">
          <div transition:fly={{ x: -200, delay: 500 }} class="p-10 text-white rounded-lg bg-black bg-opacity-50">
            <p>Our AI will analyze the ingredients and suggest recipes.</p>
            <p class="text-sm mt-4">You'll be amazed by the variety of dishes you can make!</p>
          </div>
          <div transition:fly={{ x: 200, delay: 500 }} class="flex justify-center">
            <img src="ai.png" alt="AI Analysis" class="max-w-xs rounded-lg shadow-lg">
          </div>
        </div>
      </section>
      
      
      
    <section class="h-screen flex flex-col justify-center items-center bg-gray-100 space-y-5">
      <div class="flex flex-col items-center">
        <img src="tech.png" alt="Chef AI" class="max-w-xs rounded-lg shadow-lg transition-transform duration-700" transition:fly={{ x: 200, delay: 700 }}>
        <div class="text-center mt-5 text-white p-10 rounded-lg bg-opacity-50 bg-gray-800 shadow-xl">
          <p>Our Chef AI matches recipes based on your fridge!</p>
          <p class="text-sm mt-4">Explore hundreds of recipes tailored to the ingredients you already have.</p>
        </div>
      </div>
    </section>
  
    <section class="h-screen flex flex-col justify-center items-center bg-gray-100 space-y-5">
      <div transition:fade={{ delay: 900 }} class="text-center p-10 m-5 rounded-lg bg-white shadow-lg">
        <p class="text-lg font-semibold">"Incredible app! It's like magic!" - Jane Doe</p>
        <p class="text-sm">Award of Excellence in Innovation, 2024</p>
        <p class="text-gray-600 mt-4">Join thousands of happy users revolutionizing their cooking habits.</p>
      </div>
    </section>
  </div>
  