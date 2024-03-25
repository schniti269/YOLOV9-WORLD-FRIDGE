<script>
    import {Card, Button, Label, Input, Checkbox, CloseButton} from 'flowbite-svelte';
    import {openLoginCard} from "../stores";
    import {InfoCircleSolid} from "flowbite-svelte-icons";
</script>

<div class="flex items-center justify-center px-6 py-8 mx-auto md:h-screen lg:py-0 showfront">
    <Card>
        <div class="flex items-center">
            <h5 id="drawer-label"
                class="inline-flex items-center mb-6 text-base font-semibold text-gray-500 uppercase dark:text-gray-400">
                <InfoCircleSolid class="w-4 h-4 me-2.5"/>
                Login
            </h5>
            <CloseButton on:click={() => (openLoginCard.set(false))} class="mb-4 dark:text-white"/>
        </div>
        <form class="flex flex-col space-y-6" action="/">
            <h3 class="text-xl font-medium text-gray-900 dark:text-white">Sign in to our platform</h3>
            <Label class="space-y-2">
                <span>Email</span>
                <Input type="email" name="email" placeholder="name@company.com" required/>
            </Label>
            <Label class="space-y-2">
                <span>Your password</span>
                <Input type="password" name="password" placeholder="•••••" required/>
            </Label>
            <Button type="submit" class="w-full">Login to your account</Button>
            <div class="text-sm font-medium text-gray-500 dark:text-gray-300">
                Not registered?
                <a href="/" class="text-primary-700 hover:underline dark:text-primary-500">
                    Create account
                </a>
            </div>
        </form>
    </Card>
</div>

<style>
    .showfront {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        z-index: 1000;
    }
</style>