<script lang="ts">
    import {openLoginCard} from '../stores';
    import {Button} from "flowbite-svelte";
</script>

<body>

<!-- Main container -->
<div class="min-h-screen flex items-center justify-center">
    <!-- Content wrapper -->
    <div class="max-w-6xl mx-auto p-6">
        <!-- Introduction card -->
        <div class="bg-secondary-400 rounded-lg shadow-lg p-6 text-gray-200">
            <!-- Title -->
            <h1 class="text-4xl font-bold mb-4">Willkommen zur Koch-App!</h1>
            <!-- Description -->
            <p class="text-lg mb-6">Unsere App verwendet Bilderkennung, um Ihnen Rezeptvorschläge basierend auf den
                Zutaten in Ihrem Kühlschranks zu geben. Keine Idee, was Sie kochen sollen? Kein Problem! Laden Sie
                einfach ein Bild Ihres Kühlschranks hoch und lassen Sie sich inspirieren.</p>

            <!-- Image grid -->
            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
                <!-- Example images -->
                <img src="example_1.png" alt="" class="rounded-lg shadow-lg border-2 border-accent-400">
                <img src="example_2.png" alt="" class="rounded-lg shadow-lg border-2 border-accent-400">
                <img src="example_3.png" alt="" class="rounded-lg shadow-lg border-2 border-accent-400">
            </div>
        </div>

        <!-- How it works card -->
        <div class="bg-secondary-400 rounded-lg shadow-lg p-6 mt-6 text-gray-200">
            <!-- Title -->
            <h2 class="text-3xl font-bold mb-4">Wie funktioniert es?</h2>
            <!-- Description -->
            <p class="text-lg mb-6">Unsere App analysiert Bilder Ihres Kühlschranks mithilfe von
                Bilderkennungsalgorithmen und identifiziert die darin enthaltenen Lebensmittel. Anschließend schlägt sie
                Ihnen passende Rezepte vor, die Sie mit diesen Zutaten zubereiten können.</p>

            <!-- Why our app section -->
            <h2 class="text-3xl font-bold mb-4">Warum unsere App?</h2>
            <!-- Description -->
            <p class="text-lg mb-6">Mit unserer App sparen Sie Zeit beim Kochen und vermeiden Lebensmittelverschwendung,
                indem Sie kreative Rezepte basierend auf den vorhandenen Zutaten erhalten. Außerdem bietet sie eine
                benutzerfreundliche Oberfläche und schnelle Ergebnisse.</p>

            <!-- Get started section -->
            <h2 class="text-3xl font-bold mb-4">Los geht's!</h2>
            <!-- Description -->
            <p class="text-lg mb-6">Melden Sie sich jetzt an und entdecken Sie eine neue Welt des Kochens mit unserer
                innovativen App. Laden Sie einfach ein Bild Ihres Kühlschranks hoch und lassen Sie sich von unseren
                Rezeptvorschlägen inspirieren.</p>

            <!-- Sign up button -->
            <!-- On click, the openLoginCard store is set to true, opening the login card -->
            <Button on:click={() => (openLoginCard.set(true))}
                    class="bg-secondary-600 font-bold hover:bg-secondary-300">Jetzt anmelden
            </Button>
        </div>
    </div>
</div>

</body>