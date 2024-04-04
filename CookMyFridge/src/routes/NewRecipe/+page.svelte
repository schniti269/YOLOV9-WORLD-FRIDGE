<script lang="ts">
    import {onDestroy, onMount} from "svelte";

    let stream: MediaStream | null = null;
    let videoElement: HTMLVideoElement | null = null;
    let errorMessage: string | null = null;

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
            uploadPhoto(photoDataUrl);
        }
    }

    function stopCamera() {
        stream?.getTracks().forEach(track => track.stop());
    }

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

    async function uploadPhoto(photoDataUrl: string) {
        try {
            // Make a POST request to the API endpoint
            const response = await fetch('https://example.com/api/upload-photo', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ photo: photoDataUrl })
            });
            if (!response.ok) {
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

<div class="min-h-screen flex items-center justify-center">
    <div class="max-w-2xl mx-auto p-6 bg-secondary rounded-lg shadow-lg text-white">
        <h1 class="text-3xl font-bold mb-6">Take a Photo</h1>
        <div class="relative">
            <video bind:this={videoElement} autoplay class="w-full rounded-lg shadow-md">
                <track kind="captions" src="">
            </video>
            <button on:click={capturePhoto}
                    class="absolute bottom-0 right-0 m-4 bg-blue-500 text-white px-4 py-2 rounded-lg shadow-md">Capture
            </button>
            {#if errorMessage}
                <p class="absolute bottom-0 left-0 m-4 text-red-500">{errorMessage}</p>
            {/if}
        </div>
        <div class="mt-4">
            <input type="file" accept="image/*" on:change={handleFileUpload}>
        </div>
    </div>
</div>

<style>
    video {
        height: 400px; /* Adjust the height as needed */
    }
</style>
