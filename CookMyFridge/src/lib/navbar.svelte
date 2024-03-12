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
    import {writable} from "svelte/store";

    let loggedIn = false;
    export const showLoginCard = writable(false);

    function toggleLoginCard() {
        showLoginCard.update((prev) => !prev);
    }
</script>

<Navbar class="bg-primary text-white">
    <NavBrand href="/">
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
                toggleLoginCard();
                loggedIn = true; //temporarily set
            }}>Sign in</DropdownItem>
        </Dropdown>
    {/if}
    <NavUl>
        <NavLi href="/" active={true} nonActiveClass="text-white">Home</NavLi>
        <NavLi href="#" nonActiveClass="text-white">About</NavLi>
        <NavLi href="#" nonActiveClass="text-white">Contact</NavLi>
    </NavUl>
</Navbar>