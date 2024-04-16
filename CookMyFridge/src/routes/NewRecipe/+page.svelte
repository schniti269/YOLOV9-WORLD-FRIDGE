<script lang="ts">
    import {onDestroy, onMount} from "svelte";
    import {Button} from "flowbite-svelte";
    import RecipesList from "$lib/recipesList.svelte";

    // Variables for managing the camera, video element, and error messages
    let stream: MediaStream | null = null;
    let videoElement: HTMLVideoElement | null = null;
    let errorMessage: string | null = null;

    // Variables for storing the image, items, and recipes
    let image;
    let items = [];
    let recipes = [];

    /**
     * Function to start the camera
     */
    async function startCamera() {
        try {
            stream = await navigator.mediaDevices.getUserMedia({video: true});
            if (videoElement) {
                videoElement.srcObject = stream;
            }
        } catch (e) {
            console.error('Error accessing camera:', e);
            errorMessage = 'Error accessing camera';
        }
    }

    /**
     * Function to capture a photo from the video stream
     */
    function capturePhoto() {
        const canvas = document.createElement('canvas');
        if (videoElement) {
            canvas.width = videoElement.videoWidth;
            canvas.height = videoElement.videoHeight;
            const context = canvas.getContext('2d');
            if (context) {
                context.drawImage(videoElement, 0, 0, canvas.width, canvas.height);
            }
            const photoDataUrl = canvas.toDataURL('image/png');
            // remove prefix from data URL
            const photoDataUrlWithoutPrefix = photoDataUrl.split(',')[1];
            uploadPhoto(photoDataUrlWithoutPrefix);
        }
    }

    /**
     * Function to stop the camera
     */
    function stopCamera() {
        stream?.getTracks().forEach(track => track.stop());
    }

    /**
     * Function to handle file upload
     * @param {Event} event - The file upload event
     */
    function handleFileUpload(event: Event) {
        const files = (event.target as HTMLInputElement).files;
        if (files && files.length > 0) {
            const file = files[0];
            const reader = new FileReader();
            reader.onload = (e) => {
                const photoDataUrl = e.target?.result as string;
                uploadPhoto(photoDataUrl);
            };
            reader.readAsDataURL(file);
        }
    }

    /**
     * Function to upload the photo to the API
     * @param {string} photoDataUrl - The base64 encoded photo data URL
     */
    async function uploadPhoto(photoDataUrl: string) {
        try {
            // Make a POST request to the API endpoint
            const scanResponse = await fetch('http://0.0.0.0:8000/scan', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({image64: photoDataUrl})
            });
            const scanData = await scanResponse.json();

            const itemList = scanData.items.map(item => item.name[0]);
            const recipeResponse = await fetch('http://0.0.0.0:8000/match', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(itemList)
            });
            const recipeData = await recipeResponse.json();

            if (scanResponse.ok && recipeResponse.ok) {
                // decode base64 image
                image = "data:image/jpg;base64," + scanData.image;
                items = scanData.items;

                // Recipe
                recipes = recipeData;
            } else {
                throw new Error('Failed to upload photo');
            }
            console.log('Photo uploaded successfully');
        } catch (error) {
            console.error('Error uploading photo:', error);
        }
    }

    // Start camera when component is mounted
    onMount(startCamera);

    // Stop camera when component is unmounted
    onDestroy(stopCamera);
</script>

<!-- Main container for the page -->
<div class="min-h-screen flex items-center justify-center">
    <!-- Content wrapper -->
    <div class="max-w-2xl mx-auto p-6 bg-secondary rounded-lg shadow-lg text-white">
        <!-- Relative container -->
        <div class="relative">
            <!-- If items are detected, show the processing state -->
            {#if items && items.length > 0}
                <h1 class="text-3xl font-bold mb-6">Processing:</h1>
                <!-- Show a loading message while the image is being processed -->
                {#await image}
                    <p>Loading...</p>
                    <!-- Once the image is processed, display it -->
                {:then image}
                    <!-- If the image exists, display it -->
                    {#if image}
                        <img src={image} class="w-full rounded-lg shadow-md" alt="">
                    {/if}
                {/await}
                <!-- If no items are detected, show the capture state -->
            {:else}
                <h1 class="text-3xl font-bold mb-6">Take a Photo</h1>
                <!-- Video element for the camera feed -->
                <video bind:this={videoElement} autoplay class="w-full rounded-lg shadow-md">
                    <track kind="captions" src="">
                </video>
                <!-- Capture button to take a photo -->
                <Button on:click={capturePhoto}
                        class="absolute bottom-0 right-0 m-4 bg-accent-100 text-white px-4 py-2 rounded-lg shadow-md">
                    Capture
                </Button>
                <!-- If there is an error message, display it -->
                {#if errorMessage}
                    <p class="absolute bottom-0 left-0 m-4 text-red-500">{errorMessage}</p>
                {/if}
            {/if}
        </div>
        <!-- File upload input -->
        <div class="mt-4 rounded-lg bg-accent-100">
            <input type="file" accept="image/*" on:change={handleFileUpload}>
        </div>
        <!-- If items are detected, display them -->
        {#if items && items.length > 0}
            <div class="mt-6">
                <h2 class="text-2xl font-bold mb-4">Items:</h2>
                <!-- List of detected items -->
                {#each items as item (item.name)}
                    <p>{item.name}: {item.count}</p>
                {/each}
            </div>
        {/if}
        <!-- If recipes are found, display them -->
        {#if recipes && recipes.length > 0}
            <div class="mt-8">
                <h2 class="text-2xl font-bold mb-4">Recipes:</h2>
                <!-- List of found recipes -->
                <RecipesList {recipes}/>
            </div>
        {/if}
    </div>
</div>

<!-- Styles for the video element -->
<style>
    video {
        height: 400px; /* Adjust the height as needed */
    }
</style>
