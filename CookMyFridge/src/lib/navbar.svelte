<script>
    // Importing the necessary components from the Flowbite Svelte library
    import {
        Navbar,
        NavBrand,
        NavLi,
        NavUl,
        NavHamburger,
        Avatar,
        Dropdown,
        DropdownItem,
        DropdownHeader,
        DropdownDivider
    } from 'flowbite-svelte';
    // Importing the openLoginCard store from the stores directory
    import {openLoginCard} from "../stores";

    // Variable to hold the login state of the user. It starts as false.
    let loggedIn = false;
</script>

<!-- Navbar component from the Flowbite Svelte library -->
<Navbar class="bg-primary text-white">
    <!-- Navbar brand with the logo and the name of the application -->
    <NavBrand href="/">
        <img src="/Logo.webp" alt="CookMyFridge" class="w-8 h-8 mr-2 rounded-3xl"/>
        <span class="self-center whitespace-nowrap text-xl font-semibold text-white">CookMyFridge</span>
    </NavBrand>
    <!-- Container for the avatar and the hamburger menu -->
    <div class="flex items-center md:order-2">
        <!-- Avatar component from the Flowbite Svelte library -->
        <Avatar id="avatar-menu"/>
        <!-- Hamburger menu component from the Flowbite Svelte library -->
        <NavHamburger class1="w-full md:flex md:w-auto md:order-1"/>
    </div>
    <!-- If the user is logged in, display the dropdown menu with the account options -->
    {#if loggedIn}
        <Dropdown placement="bottom" triggeredBy="#avatar-menu" class="bg-accent-100 text-white rounded">
            <DropdownHeader class="text-white">
                <span class="block text-sm">Name</span>
                <span class="block truncate text-sm font-medium">name@email.com</span>
            </DropdownHeader>
            <DropdownItem>Account</DropdownItem>
            <DropdownDivider/>
            <DropdownItem on:click={() => (loggedIn = false)}>Sign out</DropdownItem>
        </Dropdown>
        <!-- If the user is not logged in, display the dropdown menu with the sign in option -->
    {:else}
        <Dropdown placement="bottom" triggeredBy="#avatar-menu" class="bg-accent-100 text-white rounded">
            <DropdownHeader class="text-white">
                <span class="block text-sm">Welcome</span>
            </DropdownHeader>
            <DropdownItem on:click={() => {
                openLoginCard.set(true);
                loggedIn = true; //temporarily set
            }}>
                Sign in | Sign out
            </DropdownItem>
        </Dropdown>
    {/if}
    <!-- Navigation links -->
    <NavUl>
        <NavLi href="/" nonActiveClass="text-white">Home</NavLi>
        <NavLi href="/MyRecipes" nonActiveClass="text-white">My Recipes</NavLi>
        <NavLi href="/NewRecipe" nonActiveClass="text-white">New Recipe</NavLi>
    </NavUl>
</Navbar>