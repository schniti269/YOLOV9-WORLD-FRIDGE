<script>
    import "../app.css";
    import Navbar from "$lib/navbar.svelte";
    import LoginCard from "$lib/loginCard.svelte";
    import {openLoginCard} from "../stores";

    let showLoginCard = false;
    openLoginCard.subscribe(value => (showLoginCard = value));
</script>

<Navbar/>


<div class="min-h-screen min-w-screen bg-background-600">

    {#if showLoginCard}
        <LoginCard/>
    {/if}

    <slot/>

</div>