<script>
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
    import {openLoginCard} from "../stores";

    let loggedIn = false;
</script>

<Navbar class="bg-primary text-white">
    <NavBrand href="/">
        <img src="/Logo.webp" alt="CookMyFridge" class="w-8 h-8 mr-2 rounded-3xl"/>
        <span class="self-center whitespace-nowrap text-xl font-semibold text-white">CookMyFridge</span>
    </NavBrand>
    <div class="flex items-center md:order-2">
        <Avatar id="avatar-menu"/>
        <NavHamburger class1="w-full md:flex md:w-auto md:order-1"/>
    </div>
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
    <NavUl>
        <NavLi href="/" nonActiveClass="text-white">Home</NavLi>
        <NavLi href="/MyRecipes" nonActiveClass="text-white">My Recipes</NavLi>
        <NavLi href="/NewRecipe" nonActiveClass="text-white">New Recipe</NavLi>
    </NavUl>
</Navbar>