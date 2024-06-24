<p align="center"><img align="center" width="280" src="./.github/text-logo.svg#gh-dark-mode-only"/></p>
<p align="center"><img align="center" width="280" src="./.github/text-logo-light.svg#gh-light-mode-only"/></p>
<h3 align="center">Showcase your skills on your GitHub or resumé with ease!</h3>
<hr>

# Docs

- [Docs](#docs)
- [Example](#example)
- [Specifying Icons](#specifying-icons)
- [Themed Icons](#themed-icons)
- [Icons Per Line](#icons-per-line)
- [Get Icons Names](#get-icons-names)
- [Centering Icons](#centering-icons)
- [Icons List](#icons-list)
  - [💖 Support the Project](#-support-the-project)

# Example

<p align="center"><img align="center" src="./.github/example-dark.png#gh-dark-mode-only"/></p>
<p align="center"><img align="center" src="./.github/example-light.png#gh-light-mode-only"/></p>

# Specifying Icons

Copy and paste the code block below into your readme to add the skills icon element!

Change the `?i=js,html,css` to a list of your skills separated by ","s! You can find a full list of icons [here](#icons-list).

```md
![My Skills](https://go-skill-icons.vercel.app/api/icons?i=js,html,css,wasm)
```

![My Skills](https://go-skill-icons.vercel.app/api/icons?i=js,html,css,wasm)

# Themed Icons

Some icons have a dark and light themed background. You can specify which theme you want as a url parameter.

This is optional. The default theme is dark.

Change the `&theme=light` to either `dark` or `light`. The theme is the background color, so light theme has a white icon background, and dark has a black-ish.

**Light Theme Example:**

```md
![My Skills](https://go-skill-icons.vercel.app/api/icons?i=java,kotlin,nodejs,figma&theme=light)
```

![My Skills](https://go-skill-icons.vercel.app/api/icons?i=java,kotlin,nodejs&theme=light)

# Icons Per Line

You can specify how many icons you would like per line! It's an optional argument, and the default is 15.

Change the `&perline=3` to any number between 1 and 50.

```md
![My Skills](https://go-skill-icons.vercel.app/api/icons?i=aws,gcp,azure,react,vue,flutter&perline=3)
```

![My Skills](https://go-skill-icons.vercel.app/api/icons?i=aws,gcp,azure,react,vue,flutter&perline=3)

# Get Icons Names

You can get the possiblity to add the name of the icons you put to help others that doesnt know what they are by using `&titles`.

The value of `titles` is a boolean, so it should be `true` or `false`, default is `false`

```md
![My Skills](https://go-skill-icons.vercel.app/api/icons?i=rust,surrealdb,actix,yew&titles=true)
```

![My Skills](https://go-skill-icons.vercel.app/api/icons?i=rust,surrealdb,actix,yew&titles=true)

# Centering Icons

Want to center the icons in your readme? The SVGs are automatically resized, so you can do it the same way you'd normally center an image.

```html
<p align="center">
  <a href="https://go-skill-icons.vercel.app/">
    <img src="https://go-skill-icons.vercel.app/api/icons?i=git,kubernetes,docker,c,vim" />
  </a>
</p>
```

<p align="center">
  <a href="https://go-skill-icons.vercel.app/">
    <img src="https://go-skill-icons.vercel.app/api/icons?i=git,kubernetes,docker,c,vim" />
  </a>
</p>

# Icons List

Here's a list of all the icons currently supported. Feel free to open an issue to suggest icons to add!

<!-- START ICONS LIST -->
| Icon ID              | Dark Icon            | Icon ID              | Light Icon           | Icon ID              | Neutral Icon         |
| -------------------- | -------------------- | -------------------- | -------------------- | -------------------- | -------------------- |
| ableton              | <img src="./assets/ableton-dark.svg" width="48"> | ableton              | <img src="./assets/ableton-light.svg" width="48"> | ableton-auto         | <img src="./assets/ableton-auto.svg" width="48"> |
| activitypub          | <img src="./assets/activitypub-dark.svg" width="48"> | activitypub          | <img src="./assets/activitypub-light.svg" width="48"> | acrobat              | <img src="./assets/acrobat.svg" width="48"> |
| actix                | <img src="./assets/actix-dark.svg" width="48"> | actix                | <img src="./assets/actix-light.svg" width="48"> | activitypub-auto     | <img src="./assets/activitypub-auto.svg" width="48"> |
| aiscript             | <img src="./assets/aiscript-dark.svg" width="48"> | aiscript             | <img src="./assets/aiscript-light.svg" width="48"> | actix-auto           | <img src="./assets/actix-auto.svg" width="48"> |
| alchemy              | <img src="./assets/alchemy-dark.svg" width="48"> | alchemy              | <img src="./assets/alchemy-light.svg" width="48"> | adonis               | <img src="./assets/adonis.svg" width="48"> |
| alpinejs             | <img src="./assets/alpinejs-dark.svg" width="48"> | alpinejs             | <img src="./assets/alpinejs-light.svg" width="48"> | aero                 | <img src="./assets/aero.svg" width="48"> |
| anaconda             | <img src="./assets/anaconda-dark.svg" width="48"> | anaconda             | <img src="./assets/anaconda-light.svg" width="48"> | aftereffects         | <img src="./assets/aftereffects.svg" width="48"> |
| androidstudio        | <img src="./assets/androidstudio-dark.svg" width="48"> | androidstudio        | <img src="./assets/androidstudio-light.svg" width="48"> | aiscript-auto        | <img src="./assets/aiscript-auto.svg" width="48"> |
| angular              | <img src="./assets/angular-dark.svg" width="48"> | angular              | <img src="./assets/angular-light.svg" width="48"> | alchemy-auto         | <img src="./assets/alchemy-auto.svg" width="48"> |
| anss                 | <img src="./assets/anss-dark.svg" width="48"> | anss                 | <img src="./assets/anss-light.svg" width="48"> | alpinejs-auto        | <img src="./assets/alpinejs-auto.svg" width="48"> |
| appcode              | <img src="./assets/appcode-dark.svg" width="48"> | appcode              | <img src="./assets/appcode-light.svg" width="48"> | anaconda-auto        | <img src="./assets/anaconda-auto.svg" width="48"> |
| apple                | <img src="./assets/apple-dark.svg" width="48"> | apple                | <img src="./assets/apple-light.svg" width="48"> | androidstudio-auto   | <img src="./assets/androidstudio-auto.svg" width="48"> |
| aqua                 | <img src="./assets/aqua-dark.svg" width="48"> | aqua                 | <img src="./assets/aqua-light.svg" width="48"> | angular-auto         | <img src="./assets/angular-auto.svg" width="48"> |
| arch                 | <img src="./assets/arch-dark.svg" width="48"> | arch                 | <img src="./assets/arch-light.svg" width="48"> | animate              | <img src="./assets/animate.svg" width="48"> |
| argocd               | <img src="./assets/argocd-dark.svg" width="48"> | argocd               | <img src="./assets/argocd-light.svg" width="48"> | ansible              | <img src="./assets/ansible.svg" width="48"> |
| autocad              | <img src="./assets/autocad-dark.svg" width="48"> | autocad              | <img src="./assets/autocad-light.svg" width="48"> | anss-auto            | <img src="./assets/anss-auto.svg" width="48"> |
| aws                  | <img src="./assets/aws-dark.svg" width="48"> | aws                  | <img src="./assets/aws-light.svg" width="48"> | apollo               | <img src="./assets/apollo.svg" width="48"> |
| azure                | <img src="./assets/azure-dark.svg" width="48"> | azure                | <img src="./assets/azure-light.svg" width="48"> | appcode-auto         | <img src="./assets/appcode-auto.svg" width="48"> |
| bash                 | <img src="./assets/bash-dark.svg" width="48"> | bash                 | <img src="./assets/bash-light.svg" width="48"> | apple-auto           | <img src="./assets/apple-auto.svg" width="48"> |
| beeceptor            | <img src="./assets/beeceptor-dark.svg" width="48"> | beeceptor            | <img src="./assets/beeceptor-light.svg" width="48"> | appwrite             | <img src="./assets/appwrite.svg" width="48"> |
| bevy                 | <img src="./assets/bevy-dark.svg" width="48"> | bevy                 | <img src="./assets/bevy-light.svg" width="48"> | aqua-auto            | <img src="./assets/aqua-auto.svg" width="48"> |
| bitbucket            | <img src="./assets/bitbucket-dark.svg" width="48"> | bitbucket            | <img src="./assets/bitbucket-light.svg" width="48"> | arch-auto            | <img src="./assets/arch-auto.svg" width="48"> |
| blazor               | <img src="./assets/blazor-dark.svg" width="48"> | blazor               | <img src="./assets/blazor-light.svg" width="48"> | arduino              | <img src="./assets/arduino.svg" width="48"> |
| blender              | <img src="./assets/blender-dark.svg" width="48"> | blender              | <img src="./assets/blender-light.svg" width="48"> | argocd-auto          | <img src="./assets/argocd-auto.svg" width="48"> |
| brave                | <img src="./assets/brave-dark.svg" width="48"> | brave                | <img src="./assets/brave-light.svg" width="48"> | assembly             | <img src="./assets/assembly.svg" width="48"> |
| bsd                  | <img src="./assets/bsd-dark.svg" width="48"> | bsd                  | <img src="./assets/bsd-light.svg" width="48"> | astro                | <img src="./assets/astro.svg" width="48"> |
| bulma                | <img src="./assets/bulma-dark.svg" width="48"> | bulma                | <img src="./assets/bulma-light.svg" width="48"> | atom                 | <img src="./assets/atom.svg" width="48"> |
| bun                  | <img src="./assets/bun-dark.svg" width="48"> | bun                  | <img src="./assets/bun-light.svg" width="48"> | audition             | <img src="./assets/audition.svg" width="48"> |
| canva                | <img src="./assets/canva-dark.svg" width="48"> | canva                | <img src="./assets/canva-light.svg" width="48"> | autocad-auto         | <img src="./assets/autocad-auto.svg" width="48"> |
| capacitor            | <img src="./assets/capacitor-dark.svg" width="48"> | capacitor            | <img src="./assets/capacitor-light.svg" width="48"> | aws-auto             | <img src="./assets/aws-auto.svg" width="48"> |
| cassandra            | <img src="./assets/cassandra-dark.svg" width="48"> | cassandra            | <img src="./assets/cassandra-light.svg" width="48"> | azul                 | <img src="./assets/azul.svg" width="48"> |
| chatgpt              | <img src="./assets/chatgpt-dark.svg" width="48"> | chatgpt              | <img src="./assets/chatgpt-light.svg" width="48"> | azure-auto           | <img src="./assets/azure-auto.svg" width="48"> |
| chrome               | <img src="./assets/chrome-dark.svg" width="48"> | chrome               | <img src="./assets/chrome-light.svg" width="48"> | babel                | <img src="./assets/babel.svg" width="48"> |
| chromium             | <img src="./assets/chromium-dark.svg" width="48"> | chromium             | <img src="./assets/chromium-light.svg" width="48"> | bash-auto            | <img src="./assets/bash-auto.svg" width="48"> |
| circleci             | <img src="./assets/circleci-dark.svg" width="48"> | circleci             | <img src="./assets/circleci-light.svg" width="48"> | beeceptor-auto       | <img src="./assets/beeceptor-auto.svg" width="48"> |
| clion                | <img src="./assets/clion-dark.svg" width="48"> | clion                | <img src="./assets/clion-light.svg" width="48"> | behance              | <img src="./assets/behance.svg" width="48"> |
| clojure              | <img src="./assets/clojure-dark.svg" width="48"> | clojure              | <img src="./assets/clojure-light.svg" width="48"> | bevy-auto            | <img src="./assets/bevy-auto.svg" width="48"> |
| cloudflare           | <img src="./assets/cloudflare-dark.svg" width="48"> | cloudflare           | <img src="./assets/cloudflare-light.svg" width="48"> | bitbucket-auto       | <img src="./assets/bitbucket-auto.svg" width="48"> |
| cmake                | <img src="./assets/cmake-dark.svg" width="48"> | cmake                | <img src="./assets/cmake-light.svg" width="48"> | blazor-auto          | <img src="./assets/blazor-auto.svg" width="48"> |
| codeberg             | <img src="./assets/codeberg-dark.svg" width="48"> | codeberg             | <img src="./assets/codeberg-light.svg" width="48"> | blender-auto         | <img src="./assets/blender-auto.svg" width="48"> |
| codeigniter          | <img src="./assets/codeigniter-dark.svg" width="48"> | codeigniter          | <img src="./assets/codeigniter-light.svg" width="48"> | bootstrap            | <img src="./assets/bootstrap.svg" width="48"> |
| codepen              | <img src="./assets/codepen-dark.svg" width="48"> | codepen              | <img src="./assets/codepen-light.svg" width="48"> | brave-auto           | <img src="./assets/brave-auto.svg" width="48"> |
| coffeescript         | <img src="./assets/coffeescript-dark.svg" width="48"> | coffeescript         | <img src="./assets/coffeescript-light.svg" width="48"> | breeze               | <img src="./assets/breeze.svg" width="48"> |
| crystal              | <img src="./assets/crystal-dark.svg" width="48"> | crystal              | <img src="./assets/crystal-light.svg" width="48"> | bridge               | <img src="./assets/bridge.svg" width="48"> |
| cypress              | <img src="./assets/cypress-dark.svg" width="48"> | cypress              | <img src="./assets/cypress-light.svg" width="48"> | bsd-auto             | <img src="./assets/bsd-auto.svg" width="48"> |
| d3                   | <img src="./assets/d3-dark.svg" width="48"> | d3                   | <img src="./assets/d3-light.svg" width="48"> | bulma-auto           | <img src="./assets/bulma-auto.svg" width="48"> |
| dailydev             | <img src="./assets/dailydev-dark.svg" width="48"> | dailydev             | <img src="./assets/dailydev-light.svg" width="48"> | bun-auto             | <img src="./assets/bun-auto.svg" width="48"> |
| dart                 | <img src="./assets/dart-dark.svg" width="48"> | dart                 | <img src="./assets/dart-light.svg" width="48"> | c                    | <img src="./assets/c.svg" width="48"> |
| datagrip             | <img src="./assets/datagrip-dark.svg" width="48"> | databricks           | <img src="./assets/databricks-light.svg" width="48"> | canva-auto           | <img src="./assets/canva-auto.svg" width="48"> |
| dataspell            | <img src="./assets/dataspell-dark.svg" width="48"> | datagrip             | <img src="./assets/datagrip-light.svg" width="48"> | capacitor-auto       | <img src="./assets/capacitor-auto.svg" width="48"> |
| dbeaver              | <img src="./assets/dbeaver-dark.svg" width="48"> | dataspell            | <img src="./assets/dataspell-light.svg" width="48"> | capture              | <img src="./assets/capture.svg" width="48"> |
| defold               | <img src="./assets/defold-dark.svg" width="48"> | dbeaver              | <img src="./assets/dbeaver-light.svg" width="48"> | cashier              | <img src="./assets/cashier.svg" width="48"> |
| deno                 | <img src="./assets/deno-dark.svg" width="48"> | defold               | <img src="./assets/defold-light.svg" width="48"> | cassandra-auto       | <img src="./assets/cassandra-auto.svg" width="48"> |
| devto                | <img src="./assets/devto-dark.svg" width="48"> | deno                 | <img src="./assets/deno-light.svg" width="48"> | characteranimator    | <img src="./assets/characteranimator.svg" width="48"> |
| digitalocean         | <img src="./assets/digitalocean-dark.svg" width="48"> | devto                | <img src="./assets/devto-light.svg" width="48"> | chatgpt-auto         | <img src="./assets/chatgpt-auto.svg" width="48"> |
| discordjs            | <img src="./assets/discordjs-dark.svg" width="48"> | digitalocean         | <img src="./assets/digitalocean-light.svg" width="48"> | chrome-auto          | <img src="./assets/chrome-auto.svg" width="48"> |
| docksal              | <img src="./assets/docksal-dark.svg" width="48"> | discordjs            | <img src="./assets/discordjs-light.svg" width="48"> | chromium-auto        | <img src="./assets/chromium-auto.svg" width="48"> |
| drupal               | <img src="./assets/drupal-dark.svg" width="48"> | docksal              | <img src="./assets/docksal-light.svg" width="48"> | circleci-auto        | <img src="./assets/circleci-auto.svg" width="48"> |
| dynamodb             | <img src="./assets/dynamodb-dark.svg" width="48"> | drupal               | <img src="./assets/drupal-light.svg" width="48"> | clion-auto           | <img src="./assets/clion-auto.svg" width="48"> |
| eclipse              | <img src="./assets/eclipse-dark.svg" width="48"> | dynamodb             | <img src="./assets/dynamodb-light.svg" width="48"> | clojure-auto         | <img src="./assets/clojure-auto.svg" width="48"> |
| edge                 | <img src="./assets/edge-dark.svg" width="48"> | eclipse              | <img src="./assets/eclipse-light.svg" width="48"> | cloudflare-auto      | <img src="./assets/cloudflare-auto.svg" width="48"> |
| elasticsearch        | <img src="./assets/elasticsearch-dark.svg" width="48"> | edge                 | <img src="./assets/edge-light.svg" width="48"> | cmake-auto           | <img src="./assets/cmake-auto.svg" width="48"> |
| elixir               | <img src="./assets/elixir-dark.svg" width="48"> | elasticsearch        | <img src="./assets/elasticsearch-light.svg" width="48"> | codeberg-auto        | <img src="./assets/codeberg-auto.svg" width="48"> |
| elysia               | <img src="./assets/elysia-dark.svg" width="48"> | elixir               | <img src="./assets/elixir-light.svg" width="48"> | codeigniter-auto     | <img src="./assets/codeigniter-auto.svg" width="48"> |
| emotion              | <img src="./assets/emotion-dark.svg" width="48"> | elysia               | <img src="./assets/elysia-light.svg" width="48"> | codepen-auto         | <img src="./assets/codepen-auto.svg" width="48"> |
| excel                | <img src="./assets/excel-dark.svg" width="48"> | emotion              | <img src="./assets/emotion-light.svg" width="48"> | coffeescript-auto    | <img src="./assets/coffeescript-auto.svg" width="48"> |
| expressjs            | <img src="./assets/expressjs-dark.svg" width="48"> | excel                | <img src="./assets/excel-light.svg" width="48"> | cpp                  | <img src="./assets/cpp.svg" width="48"> |
| fastai               | <img src="./assets/fastai-dark.svg" width="48"> | expressjs            | <img src="./assets/expressjs-light.svg" width="48"> | creativecloud        | <img src="./assets/creativecloud.svg" width="48"> |
| fediverse            | <img src="./assets/fediverse-dark.svg" width="48"> | fastai               | <img src="./assets/fastai-light.svg" width="48"> | crystal-auto         | <img src="./assets/crystal-auto.svg" width="48"> |
| figma                | <img src="./assets/figma-dark.svg" width="48"> | fediverse            | <img src="./assets/fediverse-light.svg" width="48"> | cs                   | <img src="./assets/cs.svg" width="48"> |
| firebase             | <img src="./assets/firebase-dark.svg" width="48"> | figma                | <img src="./assets/figma-light.svg" width="48"> | css                  | <img src="./assets/css.svg" width="48"> |
| firefox              | <img src="./assets/firefox-dark.svg" width="48"> | firebase             | <img src="./assets/firebase-light.svg" width="48"> | cypress-auto         | <img src="./assets/cypress-auto.svg" width="48"> |
| flask                | <img src="./assets/flask-dark.svg" width="48"> | firefox              | <img src="./assets/firefox-light.svg" width="48"> | d                    | <img src="./assets/d.svg" width="48"> |
| fleet                | <img src="./assets/fleet-dark.svg" width="48"> | flask                | <img src="./assets/flask-light.svg" width="48"> | d3-auto              | <img src="./assets/d3-auto.svg" width="48"> |
| flutter              | <img src="./assets/flutter-dark.svg" width="48"> | fleet                | <img src="./assets/fleet-light.svg" width="48"> | dailydev-auto        | <img src="./assets/dailydev-auto.svg" width="48"> |
| ganache              | <img src="./assets/ganache-dark.svg" width="48"> | flutter              | <img src="./assets/flutter-light.svg" width="48"> | dart-auto            | <img src="./assets/dart-auto.svg" width="48"> |
| gcp                  | <img src="./assets/gcp-dark.svg" width="48"> | ganache              | <img src="./assets/ganache-light.svg" width="48"> | databricks-auto      | <img src="./assets/databricks-auto.svg" width="48"> |
| gemini               | <img src="./assets/gemini-dark.svg" width="48"> | gcp                  | <img src="./assets/gcp-light.svg" width="48"> | databricks-black     | <img src="./assets/databricks-black.svg" width="48"> |
| gherkin              | <img src="./assets/gherkin-dark.svg" width="48"> | gemini               | <img src="./assets/gemini-light.svg" width="48"> | datadog              | <img src="./assets/datadog.svg" width="48"> |
| gimp                 | <img src="./assets/gimp-dark.svg" width="48"> | gherkin              | <img src="./assets/gherkin-light.svg" width="48"> | datagrip-auto        | <img src="./assets/datagrip-auto.svg" width="48"> |
| git                  | <img src="./assets/git-dark.svg" width="48"> | gimp                 | <img src="./assets/gimp-light.svg" width="48"> | dataspell-auto       | <img src="./assets/dataspell-auto.svg" width="48"> |
| github               | <img src="./assets/github-dark.svg" width="48"> | git                  | <img src="./assets/git-light.svg" width="48"> | dbeaver-auto         | <img src="./assets/dbeaver-auto.svg" width="48"> |
| githubactions        | <img src="./assets/githubactions-dark.svg" width="48"> | github               | <img src="./assets/github-light.svg" width="48"> | debian               | <img src="./assets/debian.svg" width="48"> |
| githubcopilot        | <img src="./assets/githubcopilot-dark.svg" width="48"> | githubactions        | <img src="./assets/githubactions-light.svg" width="48"> | defold-auto          | <img src="./assets/defold-auto.svg" width="48"> |
| gitkraken            | <img src="./assets/gitkraken-dark.svg" width="48"> | githubcopilot        | <img src="./assets/githubcopilot-light.svg" width="48"> | deno-auto            | <img src="./assets/deno-auto.svg" width="48"> |
| gitlab               | <img src="./assets/gitlab-dark.svg" width="48"> | gitkraken            | <img src="./assets/gitkraken-light.svg" width="48"> | desmos               | <img src="./assets/desmos.svg" width="48"> |
| gleam                | <img src="./assets/gleam-dark.svg" width="48"> | gitlab               | <img src="./assets/gitlab-light.svg" width="48"> | devto-auto           | <img src="./assets/devto-auto.svg" width="48"> |
| gmail                | <img src="./assets/gmail-dark.svg" width="48"> | gleam                | <img src="./assets/gleam-light.svg" width="48"> | dimension            | <img src="./assets/dimension.svg" width="48"> |
| gnome                | <img src="./assets/gnome-dark.svg" width="48"> | gmail                | <img src="./assets/gmail-light.svg" width="48"> | directus             | <img src="./assets/directus.svg" width="48"> |
| godot                | <img src="./assets/godot-dark.svg" width="48"> | gnome                | <img src="./assets/gnome-light.svg" width="48"> | discord              | <img src="./assets/discord.svg" width="48"> |
| goland               | <img src="./assets/goland-dark.svg" width="48"> | godot                | <img src="./assets/godot-light.svg" width="48"> | discordbots          | <img src="./assets/discordbots.svg" width="48"> |
| googleanalytics      | <img src="./assets/googleanalytics-dark.svg" width="48"> | goland               | <img src="./assets/goland-light.svg" width="48"> | discordjs-auto       | <img src="./assets/discordjs-auto.svg" width="48"> |
| googleappsscript     | <img src="./assets/googleappsscript-dark.svg" width="48"> | googleanalytics      | <img src="./assets/googleanalytics-light.svg" width="48"> | django               | <img src="./assets/django.svg" width="48"> |
| gradle               | <img src="./assets/gradle-dark.svg" width="48"> | googleappsscript     | <img src="./assets/googleappsscript-light.svg" width="48"> | docker               | <img src="./assets/docker.svg" width="48"> |
| grafana              | <img src="./assets/grafana-dark.svg" width="48"> | gradle               | <img src="./assets/gradle-light.svg" width="48"> | docksal-auto         | <img src="./assets/docksal-auto.svg" width="48"> |
| graphql              | <img src="./assets/graphql-dark.svg" width="48"> | grafana              | <img src="./assets/grafana-light.svg" width="48"> | dotnet               | <img src="./assets/dotnet.svg" width="48"> |
| grunt                | <img src="./assets/grunt-dark.svg" width="48"> | graphql              | <img src="./assets/graphql-light.svg" width="48"> | dreamweaver          | <img src="./assets/dreamweaver.svg" width="48"> |
| gsap                 | <img src="./assets/gsap-dark.svg" width="48"> | grunt                | <img src="./assets/grunt-light.svg" width="48"> | drupal-auto          | <img src="./assets/drupal-auto.svg" width="48"> |
| gtk                  | <img src="./assets/gtk-dark.svg" width="48"> | gsap                 | <img src="./assets/gsap-light.svg" width="48"> | duckduckgo           | <img src="./assets/duckduckgo.svg" width="48"> |
| hardhat              | <img src="./assets/hardhat-dark.svg" width="48"> | gtk                  | <img src="./assets/gtk-light.svg" width="48"> | dusk                 | <img src="./assets/dusk.svg" width="48"> |
| haskell              | <img src="./assets/haskell-dark.svg" width="48"> | hardhat              | <img src="./assets/hardhat-light.svg" width="48"> | dynamodb-auto        | <img src="./assets/dynamodb-auto.svg" width="48"> |
| haxe                 | <img src="./assets/haxe-dark.svg" width="48"> | haskell              | <img src="./assets/haskell-light.svg" width="48"> | echo                 | <img src="./assets/echo.svg" width="48"> |
| haxeflixel           | <img src="./assets/haxeflixel-dark.svg" width="48"> | haxe                 | <img src="./assets/haxe-light.svg" width="48"> | eclipse-auto         | <img src="./assets/eclipse-auto.svg" width="48"> |
| helix                | <img src="./assets/helix-dark.svg" width="48"> | haxeflixel           | <img src="./assets/haxeflixel-light.svg" width="48"> | edge-auto            | <img src="./assets/edge-auto.svg" width="48"> |
| helm                 | <img src="./assets/helm-dark.svg" width="48"> | helix                | <img src="./assets/helix-light.svg" width="48"> | elasticsearch-auto   | <img src="./assets/elasticsearch-auto.svg" width="48"> |
| hibernate            | <img src="./assets/hibernate-dark.svg" width="48"> | helm                 | <img src="./assets/helm-light.svg" width="48"> | electron             | <img src="./assets/electron.svg" width="48"> |
| hono                 | <img src="./assets/hono-dark.svg" width="48"> | hibernate            | <img src="./assets/hibernate-light.svg" width="48"> | elixir-auto          | <img src="./assets/elixir-auto.svg" width="48"> |
| htmx                 | <img src="./assets/htmx-dark.svg" width="48"> | hono                 | <img src="./assets/hono-light.svg" width="48"> | elysia-auto          | <img src="./assets/elysia-auto.svg" width="48"> |
| htop                 | <img src="./assets/htop-dark.svg" width="48"> | htmx                 | <img src="./assets/htmx-light.svg" width="48"> | emacs                | <img src="./assets/emacs.svg" width="48"> |
| hydrogen             | <img src="./assets/hydrogen-dark.svg" width="48"> | htop                 | <img src="./assets/htop-light.svg" width="48"> | ember                | <img src="./assets/ember.svg" width="48"> |
| hyprland             | <img src="./assets/hyprland-dark.svg" width="48"> | hydrogen             | <img src="./assets/hydrogen-light.svg" width="48"> | emotion-auto         | <img src="./assets/emotion-auto.svg" width="48"> |
| i3                   | <img src="./assets/i3-dark.svg" width="48"> | hyprland             | <img src="./assets/hyprland-light.svg" width="48"> | envoyer              | <img src="./assets/envoyer.svg" width="48"> |
| idea                 | <img src="./assets/idea-dark.svg" width="48"> | i3                   | <img src="./assets/i3-light.svg" width="48"> | excel-auto           | <img src="./assets/excel-auto.svg" width="48"> |
| ignite               | <img src="./assets/ignite-dark.svg" width="48"> | idea                 | <img src="./assets/idea-light.svg" width="48"> | expressjs-auto       | <img src="./assets/expressjs-auto.svg" width="48"> |
| ipfs                 | <img src="./assets/ipfs-dark.svg" width="48"> | ignite               | <img src="./assets/ignite-light.svg" width="48"> | facebook             | <img src="./assets/facebook.svg" width="48"> |
| java                 | <img src="./assets/java-dark.svg" width="48"> | ipfs                 | <img src="./assets/ipfs-light.svg" width="48"> | fastai-auto          | <img src="./assets/fastai-auto.svg" width="48"> |
| jenkins              | <img src="./assets/jenkins-dark.svg" width="48"> | java                 | <img src="./assets/java-light.svg" width="48"> | fastapi              | <img src="./assets/fastapi.svg" width="48"> |
| jetpackcompose       | <img src="./assets/jetpackcompose-dark.svg" width="48"> | jenkins              | <img src="./assets/jenkins-light.svg" width="48"> | fediverse-auto       | <img src="./assets/fediverse-auto.svg" width="48"> |
| jira                 | <img src="./assets/jira-dark.svg" width="48"> | jetpackcompose       | <img src="./assets/jetpackcompose-light.svg" width="48"> | figma-auto           | <img src="./assets/figma-auto.svg" width="48"> |
| joomla               | <img src="./assets/joomla-dark.svg" width="48"> | jira                 | <img src="./assets/jira-light.svg" width="48"> | filament             | <img src="./assets/filament.svg" width="48"> |
| julia                | <img src="./assets/julia-dark.svg" width="48"> | joomla               | <img src="./assets/joomla-light.svg" width="48"> | firebase-auto        | <img src="./assets/firebase-auto.svg" width="48"> |
| kaggle               | <img src="./assets/kaggle-dark.svg" width="48"> | julia                | <img src="./assets/julia-light.svg" width="48"> | firefox-auto         | <img src="./assets/firefox-auto.svg" width="48"> |
| kakoune              | <img src="./assets/kakoune-dark.svg" width="48"> | kaggle               | <img src="./assets/kaggle-light.svg" width="48"> | flameshot            | <img src="./assets/flameshot.svg" width="48"> |
| kali                 | <img src="./assets/kali-dark.svg" width="48"> | kakoune              | <img src="./assets/kakoune-light.svg" width="48"> | flask-auto           | <img src="./assets/flask-auto.svg" width="48"> |
| kde                  | <img src="./assets/kde-dark.svg" width="48"> | kali                 | <img src="./assets/kali-light.svg" width="48"> | fleet-auto           | <img src="./assets/fleet-auto.svg" width="48"> |
| kotlin               | <img src="./assets/kotlin-dark.svg" width="48"> | kde                  | <img src="./assets/kde-light.svg" width="48"> | flutter-auto         | <img src="./assets/flutter-auto.svg" width="48"> |
| ktor                 | <img src="./assets/ktor-dark.svg" width="48"> | kotlin               | <img src="./assets/kotlin-light.svg" width="48"> | fonts                | <img src="./assets/fonts.svg" width="48"> |
| langchain            | <img src="./assets/langchain-dark.svg" width="48"> | ktor                 | <img src="./assets/ktor-light.svg" width="48"> | forge                | <img src="./assets/forge.svg" width="48"> |
| laravel              | <img src="./assets/laravel-dark.svg" width="48"> | langchain            | <img src="./assets/langchain-light.svg" width="48"> | forth                | <img src="./assets/forth.svg" width="48"> |
| laravelspark         | <img src="./assets/laravelspark-dark.svg" width="48"> | laravel              | <img src="./assets/laravel-light.svg" width="48"> | fortran              | <img src="./assets/fortran.svg" width="48"> |
| latex                | <img src="./assets/latex-dark.svg" width="48"> | laravelspark         | <img src="./assets/laravelspark-light.svg" width="48"> | fresco               | <img src="./assets/fresco.svg" width="48"> |
| leetcode             | <img src="./assets/leetcode-dark.svg" width="48"> | latex                | <img src="./assets/latex-light.svg" width="48"> | fuse                 | <img src="./assets/fuse.svg" width="48"> |
| less                 | <img src="./assets/less-dark.svg" width="48"> | leetcode             | <img src="./assets/leetcode-light.svg" width="48"> | gamemakerstudio      | <img src="./assets/gamemakerstudio.svg" width="48"> |
| lightning            | <img src="./assets/lightning-dark.svg" width="48"> | less                 | <img src="./assets/less-light.svg" width="48"> | ganache-auto         | <img src="./assets/ganache-auto.svg" width="48"> |
| linux                | <img src="./assets/linux-dark.svg" width="48"> | lightning            | <img src="./assets/lightning-light.svg" width="48"> | gatsby               | <img src="./assets/gatsby.svg" width="48"> |
| lit                  | <img src="./assets/lit-dark.svg" width="48"> | linux                | <img src="./assets/linux-light.svg" width="48"> | gcp-auto             | <img src="./assets/gcp-auto.svg" width="48"> |
| litmus               | <img src="./assets/litmus-dark.svg" width="48"> | lit                  | <img src="./assets/lit-light.svg" width="48"> | gemini-auto          | <img src="./assets/gemini-auto.svg" width="48"> |
| livewire             | <img src="./assets/livewire-dark.svg" width="48"> | litmus               | <img src="./assets/litmus-light.svg" width="48"> | gherkin-auto         | <img src="./assets/gherkin-auto.svg" width="48"> |
| looker               | <img src="./assets/looker-dark.svg" width="48"> | livewire             | <img src="./assets/livewire-light.svg" width="48"> | gimp-auto            | <img src="./assets/gimp-auto.svg" width="48"> |
| lua                  | <img src="./assets/lua-dark.svg" width="48"> | looker               | <img src="./assets/looker-light.svg" width="48"> | git-auto             | <img src="./assets/git-auto.svg" width="48"> |
| lucidchart           | <img src="./assets/lucidchart-dark.svg" width="48"> | lua                  | <img src="./assets/lua-light.svg" width="48"> | github-auto          | <img src="./assets/github-auto.svg" width="48"> |
| markdown             | <img src="./assets/markdown-dark.svg" width="48"> | lucidchart           | <img src="./assets/lucidchart-light.svg" width="48"> | githubactions-auto   | <img src="./assets/githubactions-auto.svg" width="48"> |
| mastodon             | <img src="./assets/mastodon-dark.svg" width="48"> | markdown             | <img src="./assets/markdown-light.svg" width="48"> | githubcopilot-auto   | <img src="./assets/githubcopilot-auto.svg" width="48"> |
| materialui           | <img src="./assets/materialui-dark.svg" width="48"> | mastodon             | <img src="./assets/mastodon-light.svg" width="48"> | gitkraken-auto       | <img src="./assets/gitkraken-auto.svg" width="48"> |
| matlab               | <img src="./assets/matlab-dark.svg" width="48"> | materialui           | <img src="./assets/materialui-light.svg" width="48"> | gitlab-auto          | <img src="./assets/gitlab-auto.svg" width="48"> |
| matplotlib           | <img src="./assets/matplotlib-dark.svg" width="48"> | matlab               | <img src="./assets/matlab-light.svg" width="48"> | gleam-auto           | <img src="./assets/gleam-auto.svg" width="48"> |
| maven                | <img src="./assets/maven-dark.svg" width="48"> | matplotlib           | <img src="./assets/matplotlib-light.svg" width="48"> | gmail-auto           | <img src="./assets/gmail-auto.svg" width="48"> |
| meteorjs             | <img src="./assets/meteorjs-dark.svg" width="48"> | maven                | <img src="./assets/maven-light.svg" width="48"> | gnome-auto           | <img src="./assets/gnome-auto.svg" width="48"> |
| microsoftcopilot     | <img src="./assets/microsoftcopilot-dark.svg" width="48"> | meteorjs             | <img src="./assets/meteorjs-light.svg" width="48"> | godot-auto           | <img src="./assets/godot-auto.svg" width="48"> |
| millionjs            | <img src="./assets/millionjs-dark.svg" width="48"> | microsoftcopilot     | <img src="./assets/microsoftcopilot-light.svg" width="48"> | goland-auto          | <img src="./assets/goland-auto.svg" width="48"> |
| mint                 | <img src="./assets/mint-dark.svg" width="48"> | millionjs            | <img src="./assets/millionjs-light.svg" width="48"> | golang               | <img src="./assets/golang.svg" width="48"> |
| misskey              | <img src="./assets/misskey-dark.svg" width="48"> | mint                 | <img src="./assets/mint-light.svg" width="48"> | googleanalytics-auto | <img src="./assets/googleanalytics-auto.svg" width="48"> |
| mjml                 | <img src="./assets/mjml-dark.svg" width="48"> | misskey              | <img src="./assets/misskey-light.svg" width="48"> | googleappsscript-auto | <img src="./assets/googleappsscript-auto.svg" width="48"> |
| ml5                  | <img src="./assets/ml5-dark.svg" width="48"> | mjml                 | <img src="./assets/mjml-light.svg" width="48"> | gradle-auto          | <img src="./assets/gradle-auto.svg" width="48"> |
| mojo                 | <img src="./assets/mojo-dark.svg" width="48"> | ml5                  | <img src="./assets/ml5-light.svg" width="48"> | grafana-auto         | <img src="./assets/grafana-auto.svg" width="48"> |
| mysql                | <img src="./assets/mysql-dark.svg" width="48"> | mojo                 | <img src="./assets/mojo-light.svg" width="48"> | grails               | <img src="./assets/grails.svg" width="48"> |
| neovim               | <img src="./assets/neovim-dark.svg" width="48"> | mysql                | <img src="./assets/mysql-light.svg" width="48"> | graphql-auto         | <img src="./assets/graphql-auto.svg" width="48"> |
| nestjs               | <img src="./assets/nestjs-dark.svg" width="48"> | neovim               | <img src="./assets/neovim-light.svg" width="48"> | grunt-auto           | <img src="./assets/grunt-auto.svg" width="48"> |
| netlify              | <img src="./assets/netlify-dark.svg" width="48"> | nestjs               | <img src="./assets/nestjs-light.svg" width="48"> | gsap-auto            | <img src="./assets/gsap-auto.svg" width="48"> |
| nextjs               | <img src="./assets/nextjs-dark.svg" width="48"> | netlify              | <img src="./assets/netlify-light.svg" width="48"> | gtk-auto             | <img src="./assets/gtk-auto.svg" width="48"> |
| nim                  | <img src="./assets/nim-dark.svg" width="48"> | nextjs               | <img src="./assets/nextjs-light.svg" width="48"> | gulp                 | <img src="./assets/gulp.svg" width="48"> |
| nixos                | <img src="./assets/nixos-dark.svg" width="48"> | nim                  | <img src="./assets/nim-light.svg" width="48"> | hardhat-auto         | <img src="./assets/hardhat-auto.svg" width="48"> |
| nodejs               | <img src="./assets/nodejs-dark.svg" width="48"> | nixos                | <img src="./assets/nixos-light.svg" width="48"> | haskell-auto         | <img src="./assets/haskell-auto.svg" width="48"> |
| notion               | <img src="./assets/notion-dark.svg" width="48"> | nodejs               | <img src="./assets/nodejs-light.svg" width="48"> | haxe-auto            | <img src="./assets/haxe-auto.svg" width="48"> |
| npm                  | <img src="./assets/npm-dark.svg" width="48"> | notion               | <img src="./assets/notion-light.svg" width="48"> | haxeflixel-auto      | <img src="./assets/haxeflixel-auto.svg" width="48"> |
| numpy                | <img src="./assets/numpy-dark.svg" width="48"> | npm                  | <img src="./assets/npm-light.svg" width="48"> | helix-auto           | <img src="./assets/helix-auto.svg" width="48"> |
| nuxtjs               | <img src="./assets/nuxtjs-dark.svg" width="48"> | numpy                | <img src="./assets/numpy-light.svg" width="48"> | helm-auto            | <img src="./assets/helm-auto.svg" width="48"> |
| obsidian             | <img src="./assets/obsidian-dark.svg" width="48"> | nuxtjs               | <img src="./assets/nuxtjs-light.svg" width="48"> | herd                 | <img src="./assets/herd.svg" width="48"> |
| octave               | <img src="./assets/octave-dark.svg" width="48"> | obsidian             | <img src="./assets/obsidian-light.svg" width="48"> | heroku               | <img src="./assets/heroku.svg" width="48"> |
| ollama               | <img src="./assets/ollama-dark.svg" width="48"> | octave               | <img src="./assets/octave-light.svg" width="48"> | hibernate-auto       | <img src="./assets/hibernate-auto.svg" width="48"> |
| onedrive             | <img src="./assets/onedrive-dark.svg" width="48"> | ollama               | <img src="./assets/ollama-light.svg" width="48"> | holyc                | <img src="./assets/holyc.svg" width="48"> |
| onenote              | <img src="./assets/onenote-dark.svg" width="48"> | onedrive             | <img src="./assets/onedrive-light.svg" width="48"> | hono-auto            | <img src="./assets/hono-auto.svg" width="48"> |
| opencv               | <img src="./assets/opencv-dark.svg" width="48"> | onenote              | <img src="./assets/onenote-light.svg" width="48"> | horizon              | <img src="./assets/horizon.svg" width="48"> |
| openstack            | <img src="./assets/openstack-dark.svg" width="48"> | opencv               | <img src="./assets/opencv-light.svg" width="48"> | html                 | <img src="./assets/html.svg" width="48"> |
| openzeppelin         | <img src="./assets/openzeppelin-dark.svg" width="48"> | openstack            | <img src="./assets/openstack-light.svg" width="48"> | htmx-auto            | <img src="./assets/htmx-auto.svg" width="48"> |
| opera                | <img src="./assets/opera-dark.svg" width="48"> | openzeppelin         | <img src="./assets/openzeppelin-light.svg" width="48"> | htop-auto            | <img src="./assets/htop-auto.svg" width="48"> |
| oracle               | <img src="./assets/oracle-dark.svg" width="48"> | opera                | <img src="./assets/opera-light.svg" width="48"> | hydrogen-auto        | <img src="./assets/hydrogen-auto.svg" width="48"> |
| outlook              | <img src="./assets/outlook-dark.svg" width="48"> | oracle               | <img src="./assets/oracle-light.svg" width="48"> | hyprland-auto        | <img src="./assets/hyprland-auto.svg" width="48"> |
| pail                 | <img src="./assets/pail-dark.svg" width="48"> | outlook              | <img src="./assets/outlook-light.svg" width="48"> | i3-auto              | <img src="./assets/i3-auto.svg" width="48"> |
| pandas               | <img src="./assets/pandas-dark.svg" width="48"> | pail                 | <img src="./assets/pail-light.svg" width="48"> | idea-auto            | <img src="./assets/idea-auto.svg" width="48"> |
| payload              | <img src="./assets/payload-dark.svg" width="48"> | pandas               | <img src="./assets/pandas-light.svg" width="48"> | ignite-auto          | <img src="./assets/ignite-auto.svg" width="48"> |
| pbi                  | <img src="./assets/pbi-dark.svg" width="48"> | payload              | <img src="./assets/payload-light.svg" width="48"> | illustrator          | <img src="./assets/illustrator.svg" width="48"> |
| php                  | <img src="./assets/php-dark.svg" width="48"> | pbi                  | <img src="./assets/pbi-light.svg" width="48"> | incopy               | <img src="./assets/incopy.svg" width="48"> |
| phpstorm             | <img src="./assets/phpstorm-dark.svg" width="48"> | php                  | <img src="./assets/php-light.svg" width="48"> | indesign             | <img src="./assets/indesign.svg" width="48"> |
| picocss              | <img src="./assets/picocss-dark.svg" width="48"> | phpstorm             | <img src="./assets/phpstorm-light.svg" width="48"> | inertia              | <img src="./assets/inertia.svg" width="48"> |
| pinecone             | <img src="./assets/pinecone-dark.svg" width="48"> | picocss              | <img src="./assets/picocss-light.svg" width="48"> | infura               | <img src="./assets/infura.svg" width="48"> |
| pinia                | <img src="./assets/pinia-dark.svg" width="48"> | pinecone             | <img src="./assets/pinecone-light.svg" width="48"> | insomnia             | <img src="./assets/insomnia.svg" width="48"> |
| pkl                  | <img src="./assets/pkl-dark.svg" width="48"> | pinia                | <img src="./assets/pinia-light.svg" width="48"> | instagram            | <img src="./assets/instagram.svg" width="48"> |
| plan9                | <img src="./assets/plan9-dark.svg" width="48"> | pkl                  | <img src="./assets/pkl-light.svg" width="48"> | ipfs-auto            | <img src="./assets/ipfs-auto.svg" width="48"> |
| planetscale          | <img src="./assets/planetscale-dark.svg" width="48"> | plan9                | <img src="./assets/plan9-light.svg" width="48"> | java-auto            | <img src="./assets/java-auto.svg" width="48"> |
| playwright           | <img src="./assets/playwright-dark.svg" width="48"> | planetscale          | <img src="./assets/planetscale-light.svg" width="48"> | javascript           | <img src="./assets/javascript.svg" width="48"> |
| pnpm                 | <img src="./assets/pnpm-dark.svg" width="48"> | playwright           | <img src="./assets/playwright-light.svg" width="48"> | jenkins-auto         | <img src="./assets/jenkins-auto.svg" width="48"> |
| pocketbase           | <img src="./assets/pocketbase-dark.svg" width="48"> | pnpm                 | <img src="./assets/pnpm-light.svg" width="48"> | jest                 | <img src="./assets/jest.svg" width="48"> |
| postgresql           | <img src="./assets/postgresql-dark.svg" width="48"> | pocketbase           | <img src="./assets/pocketbase-light.svg" width="48"> | jetpackcompose-auto  | <img src="./assets/jetpackcompose-auto.svg" width="48"> |
| powerpoint           | <img src="./assets/powerpoint-dark.svg" width="48"> | postgresql           | <img src="./assets/postgresql-light.svg" width="48"> | jetstream            | <img src="./assets/jetstream.svg" width="48"> |
| powershell           | <img src="./assets/powershell-dark.svg" width="48"> | powerpoint           | <img src="./assets/powerpoint-light.svg" width="48"> | jira-auto            | <img src="./assets/jira-auto.svg" width="48"> |
| preact               | <img src="./assets/preact-dark.svg" width="48"> | powershell           | <img src="./assets/powershell-light.svg" width="48"> | joomla-auto          | <img src="./assets/joomla-auto.svg" width="48"> |
| processing           | <img src="./assets/processing-dark.svg" width="48"> | preact               | <img src="./assets/preact-light.svg" width="48"> | jquery               | <img src="./assets/jquery.svg" width="48"> |
| proton               | <img src="./assets/proton-dark.svg" width="48"> | processing           | <img src="./assets/processing-light.svg" width="48"> | julia-auto           | <img src="./assets/julia-auto.svg" width="48"> |
| proxmox              | <img src="./assets/proxmox-dark.svg" width="48"> | proton               | <img src="./assets/proton-light.svg" width="48"> | kafka                | <img src="./assets/kafka.svg" width="48"> |
| pug                  | <img src="./assets/pug-dark.svg" width="48"> | proxmox              | <img src="./assets/proxmox-light.svg" width="48"> | kaggle-auto          | <img src="./assets/kaggle-auto.svg" width="48"> |
| pulse                | <img src="./assets/pulse-dark.svg" width="48"> | pug                  | <img src="./assets/pug-light.svg" width="48"> | kakoune-auto         | <img src="./assets/kakoune-auto.svg" width="48"> |
| puppeteer            | <img src="./assets/puppeteer-dark.svg" width="48"> | pulse                | <img src="./assets/pulse-light.svg" width="48"> | kali-auto            | <img src="./assets/kali-auto.svg" width="48"> |
| pycharm              | <img src="./assets/pycharm-dark.svg" width="48"> | puppeteer            | <img src="./assets/puppeteer-light.svg" width="48"> | kde-auto             | <img src="./assets/kde-auto.svg" width="48"> |
| python               | <img src="./assets/python-dark.svg" width="48"> | pycharm              | <img src="./assets/pycharm-light.svg" width="48"> | keycloak             | <img src="./assets/keycloak.svg" width="48"> |
| pytorch              | <img src="./assets/pytorch-dark.svg" width="48"> | python               | <img src="./assets/python-light.svg" width="48"> | kotlin-auto          | <img src="./assets/kotlin-auto.svg" width="48"> |
| pyxel                | <img src="./assets/pyxel-dark.svg" width="48"> | pytorch              | <img src="./assets/pytorch-light.svg" width="48"> | ktor-auto            | <img src="./assets/ktor-auto.svg" width="48"> |
| qodana               | <img src="./assets/qodana-dark.svg" width="48"> | pyxel                | <img src="./assets/pyxel-light.svg" width="48"> | kubernetes           | <img src="./assets/kubernetes.svg" width="48"> |
| qt                   | <img src="./assets/qt-dark.svg" width="48"> | qodana               | <img src="./assets/qodana-light.svg" width="48"> | langchain-auto       | <img src="./assets/langchain-auto.svg" width="48"> |
| r                    | <img src="./assets/r-dark.svg" width="48"> | qt                   | <img src="./assets/qt-light.svg" width="48"> | laravel-auto         | <img src="./assets/laravel-auto.svg" width="48"> |
| rabbitmq             | <img src="./assets/rabbitmq-dark.svg" width="48"> | r                    | <img src="./assets/r-light.svg" width="48"> | laravelspark-auto    | <img src="./assets/laravelspark-auto.svg" width="48"> |
| raspberrypi          | <img src="./assets/raspberrypi-dark.svg" width="48"> | rabbitmq             | <img src="./assets/rabbitmq-light.svg" width="48"> | latex-auto           | <img src="./assets/latex-auto.svg" width="48"> |
| react                | <img src="./assets/react-dark.svg" width="48"> | raspberrypi          | <img src="./assets/raspberrypi-light.svg" width="48"> | leetcode-auto        | <img src="./assets/leetcode-auto.svg" width="48"> |
| reactivex            | <img src="./assets/reactivex-dark.svg" width="48"> | react                | <img src="./assets/react-light.svg" width="48"> | less-auto            | <img src="./assets/less-auto.svg" width="48"> |
| reactquery           | <img src="./assets/reactquery-dark.svg" width="48"> | reactivex            | <img src="./assets/reactivex-light.svg" width="48"> | lightning-auto       | <img src="./assets/lightning-auto.svg" width="48"> |
| redhat               | <img src="./assets/redhat-dark.svg" width="48"> | reactquery           | <img src="./assets/reactquery-light.svg" width="48"> | lightroom            | <img src="./assets/lightroom.svg" width="48"> |
| redis                | <img src="./assets/redis-dark.svg" width="48"> | redhat               | <img src="./assets/redhat-light.svg" width="48"> | lightroomclassic     | <img src="./assets/lightroomclassic.svg" width="48"> |
| redshift             | <img src="./assets/redshift-dark.svg" width="48"> | redis                | <img src="./assets/redis-light.svg" width="48"> | linkedin             | <img src="./assets/linkedin.svg" width="48"> |
| regex                | <img src="./assets/regex-dark.svg" width="48"> | redshift             | <img src="./assets/redshift-light.svg" width="48"> | linux-auto           | <img src="./assets/linux-auto.svg" width="48"> |
| remix                | <img src="./assets/remix-dark.svg" width="48"> | regex                | <img src="./assets/regex-light.svg" width="48"> | lit-auto             | <img src="./assets/lit-auto.svg" width="48"> |
| replit               | <img src="./assets/replit-dark.svg" width="48"> | remix                | <img src="./assets/remix-light.svg" width="48"> | litmus-auto          | <img src="./assets/litmus-auto.svg" width="48"> |
| resharper            | <img src="./assets/resharper-dark.svg" width="48"> | replit               | <img src="./assets/replit-light.svg" width="48"> | livewire-auto        | <img src="./assets/livewire-auto.svg" width="48"> |
| rider                | <img src="./assets/rider-dark.svg" width="48"> | resharper            | <img src="./assets/resharper-light.svg" width="48"> | looker-auto          | <img src="./assets/looker-auto.svg" width="48"> |
| rollupjs             | <img src="./assets/rollupjs-dark.svg" width="48"> | rider                | <img src="./assets/rider-light.svg" width="48"> | lua-auto             | <img src="./assets/lua-auto.svg" width="48"> |
| ros                  | <img src="./assets/ros-dark.svg" width="48"> | rollupjs             | <img src="./assets/rollupjs-light.svg" width="48"> | lucidchart-auto      | <img src="./assets/lucidchart-auto.svg" width="48"> |
| rubocop              | <img src="./assets/rubocop-dark.svg" width="48"> | ros                  | <img src="./assets/ros-light.svg" width="48"> | manjaro              | <img src="./assets/manjaro.svg" width="48"> |
| rubymine             | <img src="./assets/rubymine-dark.svg" width="48"> | rubocop              | <img src="./assets/rubocop-light.svg" width="48"> | markdown-auto        | <img src="./assets/markdown-auto.svg" width="48"> |
| rust                 | <img src="./assets/rust-dark.svg" width="48"> | rubymine             | <img src="./assets/rubymine-light.svg" width="48"> | mastodon-auto        | <img src="./assets/mastodon-auto.svg" width="48"> |
| rustrover            | <img src="./assets/rustrover-dark.svg" width="48"> | rust                 | <img src="./assets/rust-light.svg" width="48"> | materialui-auto      | <img src="./assets/materialui-auto.svg" width="48"> |
| safari               | <img src="./assets/safari-dark.svg" width="48"> | rustrover            | <img src="./assets/rustrover-light.svg" width="48"> | matlab-auto          | <img src="./assets/matlab-auto.svg" width="48"> |
| scala                | <img src="./assets/scala-dark.svg" width="48"> | safari               | <img src="./assets/safari-light.svg" width="48"> | matplotlib-auto      | <img src="./assets/matplotlib-auto.svg" width="48"> |
| scikitlearn          | <img src="./assets/scikitlearn-dark.svg" width="48"> | scala                | <img src="./assets/scala-light.svg" width="48"> | maven-auto           | <img src="./assets/maven-auto.svg" width="48"> |
| scipy                | <img src="./assets/scipy-dark.svg" width="48"> | scikitlearn          | <img src="./assets/scikitlearn-light.svg" width="48"> | mediaencoder         | <img src="./assets/mediaencoder.svg" width="48"> |
| seaborn              | <img src="./assets/seaborn-dark.svg" width="48"> | scipy                | <img src="./assets/scipy-light.svg" width="48"> | mermaid              | <img src="./assets/mermaid.svg" width="48"> |
| sequelize            | <img src="./assets/sequelize-dark.svg" width="48"> | seaborn              | <img src="./assets/seaborn-light.svg" width="48"> | meteorjs-auto        | <img src="./assets/meteorjs-auto.svg" width="48"> |
| sharepoint           | <img src="./assets/sharepoint-dark.svg" width="48"> | sequelize            | <img src="./assets/sequelize-light.svg" width="48"> | microsoftcopilot-auto | <img src="./assets/microsoftcopilot-auto.svg" width="48"> |
| shopify              | <img src="./assets/shopify-dark.svg" width="48"> | sharepoint           | <img src="./assets/sharepoint-light.svg" width="48"> | millionjs-auto       | <img src="./assets/millionjs-auto.svg" width="48"> |
| skeletonui           | <img src="./assets/skeletonui-dark.svg" width="48"> | shopify              | <img src="./assets/shopify-light.svg" width="48"> | mint-auto            | <img src="./assets/mint-auto.svg" width="48"> |
| sketchup             | <img src="./assets/sketchup-dark.svg" width="48"> | skeletonui           | <img src="./assets/skeletonui-light.svg" width="48"> | miro                 | <img src="./assets/miro.svg" width="48"> |
| slack                | <img src="./assets/slack-dark.svg" width="48"> | sketchup             | <img src="./assets/sketchup-light.svg" width="48"> | misskey-auto         | <img src="./assets/misskey-auto.svg" width="48"> |
| snowflake            | <img src="./assets/snowflake-dark.svg" width="48"> | slack                | <img src="./assets/slack-light.svg" width="48"> | mjml-auto            | <img src="./assets/mjml-auto.svg" width="48"> |
| snyk                 | <img src="./assets/snyk-dark.svg" width="48"> | snowflake            | <img src="./assets/snowflake-light.svg" width="48"> | ml5-auto             | <img src="./assets/ml5-auto.svg" width="48"> |
| solidjs              | <img src="./assets/solidjs-dark.svg" width="48"> | snyk                 | <img src="./assets/snyk-light.svg" width="48"> | mojo-auto            | <img src="./assets/mojo-auto.svg" width="48"> |
| spring               | <img src="./assets/spring-dark.svg" width="48"> | solidjs              | <img src="./assets/solidjs-light.svg" width="48"> | mongodb              | <img src="./assets/mongodb.svg" width="48"> |
| sqlserver            | <img src="./assets/sqlserver-dark.svg" width="48"> | spring               | <img src="./assets/spring-light.svg" width="48"> | mysql-auto           | <img src="./assets/mysql-auto.svg" width="48"> |
| stackoverflow        | <img src="./assets/stackoverflow-dark.svg" width="48"> | sqlserver            | <img src="./assets/sqlserver-light.svg" width="48"> | neovim-auto          | <img src="./assets/neovim-auto.svg" width="48"> |
| storyblok            | <img src="./assets/storyblok-dark.svg" width="48"> | stackoverflow        | <img src="./assets/stackoverflow-light.svg" width="48"> | nestjs-auto          | <img src="./assets/nestjs-auto.svg" width="48"> |
| storybook            | <img src="./assets/storybook-dark.svg" width="48"> | storyblok            | <img src="./assets/storyblok-light.svg" width="48"> | netlify-auto         | <img src="./assets/netlify-auto.svg" width="48"> |
| streamlit            | <img src="./assets/streamlit-dark.svg" width="48"> | storybook            | <img src="./assets/storybook-light.svg" width="48"> | nextjs-auto          | <img src="./assets/nextjs-auto.svg" width="48"> |
| sublime              | <img src="./assets/sublime-dark.svg" width="48"> | streamlit            | <img src="./assets/streamlit-light.svg" width="48"> | nginx                | <img src="./assets/nginx.svg" width="48"> |
| supabase             | <img src="./assets/supabase-dark.svg" width="48"> | sublime              | <img src="./assets/sublime-light.svg" width="48"> | ngrok                | <img src="./assets/ngrok.svg" width="48"> |
| surrealdb            | <img src="./assets/surrealdb-dark.svg" width="48"> | supabase             | <img src="./assets/supabase-light.svg" width="48"> | nim-auto             | <img src="./assets/nim-auto.svg" width="48"> |
| svg                  | <img src="./assets/svg-dark.svg" width="48"> | surrealdb            | <img src="./assets/surrealdb-light.svg" width="48"> | nixos-auto           | <img src="./assets/nixos-auto.svg" width="48"> |
| swagger              | <img src="./assets/swagger-dark.svg" width="48"> | svg                  | <img src="./assets/svg-light.svg" width="48"> | nodejs-auto          | <img src="./assets/nodejs-auto.svg" width="48"> |
| symfony              | <img src="./assets/symfony-dark.svg" width="48"> | swagger              | <img src="./assets/swagger-light.svg" width="48"> | notion-auto          | <img src="./assets/notion-auto.svg" width="48"> |
| tableau              | <img src="./assets/tableau-dark.svg" width="48"> | symfony              | <img src="./assets/symfony-light.svg" width="48"> | nova                 | <img src="./assets/nova.svg" width="48"> |
| tailwindcss          | <img src="./assets/tailwindcss-dark.svg" width="48"> | tableau              | <img src="./assets/tableau-light.svg" width="48"> | npm-auto             | <img src="./assets/npm-auto.svg" width="48"> |
| tauri                | <img src="./assets/tauri-dark.svg" width="48"> | tailwindcss          | <img src="./assets/tailwindcss-light.svg" width="48"> | numpy-auto           | <img src="./assets/numpy-auto.svg" width="48"> |
| teams                | <img src="./assets/teams-dark.svg" width="48"> | tauri                | <img src="./assets/tauri-light.svg" width="48"> | nuxtjs-auto          | <img src="./assets/nuxtjs-auto.svg" width="48"> |
| tensorflow           | <img src="./assets/tensorflow-dark.svg" width="48"> | teams                | <img src="./assets/teams-light.svg" width="48"> | obsidian-auto        | <img src="./assets/obsidian-auto.svg" width="48"> |
| terraform            | <img src="./assets/terraform-dark.svg" width="48"> | tensorflow           | <img src="./assets/tensorflow-light.svg" width="48"> | ocaml                | <img src="./assets/ocaml.svg" width="48"> |
| testinglibrary       | <img src="./assets/testinglibrary-dark.svg" width="48"> | terraform            | <img src="./assets/terraform-light.svg" width="48"> | octane               | <img src="./assets/octane.svg" width="48"> |
| threejs              | <img src="./assets/threejs-dark.svg" width="48"> | testinglibrary       | <img src="./assets/testinglibrary-light.svg" width="48"> | octave-auto          | <img src="./assets/octave-auto.svg" width="48"> |
| tor                  | <img src="./assets/tor-dark.svg" width="48"> | threejs              | <img src="./assets/threejs-light.svg" width="48"> | ollama-auto          | <img src="./assets/ollama-auto.svg" width="48"> |
| truffle              | <img src="./assets/truffle-dark.svg" width="48"> | tor                  | <img src="./assets/tor-light.svg" width="48"> | onedrive-auto        | <img src="./assets/onedrive-auto.svg" width="48"> |
| unity                | <img src="./assets/unity-dark.svg" width="48"> | truffle              | <img src="./assets/truffle-light.svg" width="48"> | onenote-auto         | <img src="./assets/onenote-auto.svg" width="48"> |
| v                    | <img src="./assets/v-dark.svg" width="48"> | unity                | <img src="./assets/unity-light.svg" width="48"> | opencv-auto          | <img src="./assets/opencv-auto.svg" width="48"> |
| vercel               | <img src="./assets/vercel-dark.svg" width="48"> | v                    | <img src="./assets/v-light.svg" width="48"> | openshift            | <img src="./assets/openshift.svg" width="48"> |
| vim                  | <img src="./assets/vim-dark.svg" width="48"> | vercel               | <img src="./assets/vercel-light.svg" width="48"> | openstack-auto       | <img src="./assets/openstack-auto.svg" width="48"> |
| visualbasic          | <img src="./assets/visualbasic-dark.svg" width="48"> | vim                  | <img src="./assets/vim-light.svg" width="48"> | openzeppelin-auto    | <img src="./assets/openzeppelin-auto.svg" width="48"> |
| visualstudio         | <img src="./assets/visualstudio-dark.svg" width="48"> | visualbasic          | <img src="./assets/visualbasic-light.svg" width="48"> | opera-auto           | <img src="./assets/opera-auto.svg" width="48"> |
| vite                 | <img src="./assets/vite-dark.svg" width="48"> | visualstudio         | <img src="./assets/visualstudio-light.svg" width="48"> | oracle-auto          | <img src="./assets/oracle-auto.svg" width="48"> |
| vitest               | <img src="./assets/vitest-dark.svg" width="48"> | vite                 | <img src="./assets/vite-light.svg" width="48"> | outlook-auto         | <img src="./assets/outlook-auto.svg" width="48"> |
| vscode               | <img src="./assets/vscode-dark.svg" width="48"> | vitest               | <img src="./assets/vitest-light.svg" width="48"> | p5js                 | <img src="./assets/p5js.svg" width="48"> |
| vscodium             | <img src="./assets/vscodium-dark.svg" width="48"> | vscode               | <img src="./assets/vscode-light.svg" width="48"> | pail-auto            | <img src="./assets/pail-auto.svg" width="48"> |
| vuejs                | <img src="./assets/vuejs-dark.svg" width="48"> | vscodium             | <img src="./assets/vscodium-light.svg" width="48"> | pandas-auto          | <img src="./assets/pandas-auto.svg" width="48"> |
| vuetify              | <img src="./assets/vuetify-dark.svg" width="48"> | vuejs                | <img src="./assets/vuejs-light.svg" width="48"> | papertrail           | <img src="./assets/papertrail.svg" width="48"> |
| vyper                | <img src="./assets/vyper-dark.svg" width="48"> | vuetify              | <img src="./assets/vuetify-light.svg" width="48"> | payload-auto         | <img src="./assets/payload-auto.svg" width="48"> |
| webpack              | <img src="./assets/webpack-dark.svg" width="48"> | vyper                | <img src="./assets/vyper-light.svg" width="48"> | pbi-auto             | <img src="./assets/pbi-auto.svg" width="48"> |
| webstorm             | <img src="./assets/webstorm-dark.svg" width="48"> | webpack              | <img src="./assets/webpack-light.svg" width="48"> | pennant              | <img src="./assets/pennant.svg" width="48"> |
| windicss             | <img src="./assets/windicss-dark.svg" width="48"> | webstorm             | <img src="./assets/webstorm-light.svg" width="48"> | perl                 | <img src="./assets/perl.svg" width="48"> |
| windows              | <img src="./assets/windows-dark.svg" width="48"> | windicss             | <img src="./assets/windicss-light.svg" width="48"> | photoshop            | <img src="./assets/photoshop.svg" width="48"> |
| word                 | <img src="./assets/word-dark.svg" width="48"> | windows              | <img src="./assets/windows-light.svg" width="48"> | photoshopclassic     | <img src="./assets/photoshopclassic.svg" width="48"> |
| workers              | <img src="./assets/workers-dark.svg" width="48"> | word                 | <img src="./assets/word-light.svg" width="48"> | photoshopexpress     | <img src="./assets/photoshopexpress.svg" width="48"> |
| x                    | <img src="./assets/x-dark.svg" width="48"> | workers              | <img src="./assets/workers-light.svg" width="48"> | php-auto             | <img src="./assets/php-auto.svg" width="48"> |
| xcode                | <img src="./assets/xcode-dark.svg" width="48"> | x                    | <img src="./assets/x-light.svg" width="48"> | phpstorm-auto        | <img src="./assets/phpstorm-auto.svg" width="48"> |
| yaml                 | <img src="./assets/yaml-dark.svg" width="48"> | xcode                | <img src="./assets/xcode-light.svg" width="48"> | picocss-auto         | <img src="./assets/picocss-auto.svg" width="48"> |
| yammer               | <img src="./assets/yammer-dark.svg" width="48"> | yaml                 | <img src="./assets/yaml-light.svg" width="48"> | pinecone-auto        | <img src="./assets/pinecone-auto.svg" width="48"> |
| yarn                 | <img src="./assets/yarn-dark.svg" width="48"> | yammer               | <img src="./assets/yammer-light.svg" width="48"> | pinia-auto           | <img src="./assets/pinia-auto.svg" width="48"> |
| yew                  | <img src="./assets/yew-dark.svg" width="48"> | yarn                 | <img src="./assets/yarn-light.svg" width="48"> | pint                 | <img src="./assets/pint.svg" width="48"> |
| zed                  | <img src="./assets/zed-dark.svg" width="48"> | yew                  | <img src="./assets/yew-light.svg" width="48"> | pkl-auto             | <img src="./assets/pkl-auto.svg" width="48"> |
| zig                  | <img src="./assets/zig-dark.svg" width="48"> | zed                  | <img src="./assets/zed-light.svg" width="48"> | plan9-auto           | <img src="./assets/plan9-auto.svg" width="48"> |
|                      |                      | zig                  | <img src="./assets/zig-light.svg" width="48"> | planetscale-auto     | <img src="./assets/planetscale-auto.svg" width="48"> |
|                      |                      |                      |                      | playwright-auto      | <img src="./assets/playwright-auto.svg" width="48"> |
|                      |                      |                      |                      | pnpm-auto            | <img src="./assets/pnpm-auto.svg" width="48"> |
|                      |                      |                      |                      | pocketbase-auto      | <img src="./assets/pocketbase-auto.svg" width="48"> |
|                      |                      |                      |                      | popos                | <img src="./assets/popos.svg" width="48"> |
|                      |                      |                      |                      | portfolio            | <img src="./assets/portfolio.svg" width="48"> |
|                      |                      |                      |                      | postgresql-auto      | <img src="./assets/postgresql-auto.svg" width="48"> |
|                      |                      |                      |                      | postman              | <img src="./assets/postman.svg" width="48"> |
|                      |                      |                      |                      | powerpoint-auto      | <img src="./assets/powerpoint-auto.svg" width="48"> |
|                      |                      |                      |                      | powershell-auto      | <img src="./assets/powershell-auto.svg" width="48"> |
|                      |                      |                      |                      | preact-auto          | <img src="./assets/preact-auto.svg" width="48"> |
|                      |                      |                      |                      | prelude              | <img src="./assets/prelude.svg" width="48"> |
|                      |                      |                      |                      | premiere             | <img src="./assets/premiere.svg" width="48"> |
|                      |                      |                      |                      | premiererush         | <img src="./assets/premiererush.svg" width="48"> |
|                      |                      |                      |                      | prisma               | <img src="./assets/prisma.svg" width="48"> |
|                      |                      |                      |                      | processing-auto      | <img src="./assets/processing-auto.svg" width="48"> |
|                      |                      |                      |                      | prometheus           | <img src="./assets/prometheus.svg" width="48"> |
|                      |                      |                      |                      | prompts              | <img src="./assets/prompts.svg" width="48"> |
|                      |                      |                      |                      | proton-auto          | <img src="./assets/proton-auto.svg" width="48"> |
|                      |                      |                      |                      | proxmox-auto         | <img src="./assets/proxmox-auto.svg" width="48"> |
|                      |                      |                      |                      | pug-auto             | <img src="./assets/pug-auto.svg" width="48"> |
|                      |                      |                      |                      | pulse-auto           | <img src="./assets/pulse-auto.svg" width="48"> |
|                      |                      |                      |                      | puppeteer-auto       | <img src="./assets/puppeteer-auto.svg" width="48"> |
|                      |                      |                      |                      | pycharm-auto         | <img src="./assets/pycharm-auto.svg" width="48"> |
|                      |                      |                      |                      | python-auto          | <img src="./assets/python-auto.svg" width="48"> |
|                      |                      |                      |                      | pytorch-auto         | <img src="./assets/pytorch-auto.svg" width="48"> |
|                      |                      |                      |                      | pyxel-auto           | <img src="./assets/pyxel-auto.svg" width="48"> |
|                      |                      |                      |                      | qodana-auto          | <img src="./assets/qodana-auto.svg" width="48"> |
|                      |                      |                      |                      | qt-auto              | <img src="./assets/qt-auto.svg" width="48"> |
|                      |                      |                      |                      | r-auto               | <img src="./assets/r-auto.svg" width="48"> |
|                      |                      |                      |                      | rabbitmq-auto        | <img src="./assets/rabbitmq-auto.svg" width="48"> |
|                      |                      |                      |                      | rails                | <img src="./assets/rails.svg" width="48"> |
|                      |                      |                      |                      | raspberrypi-auto     | <img src="./assets/raspberrypi-auto.svg" width="48"> |
|                      |                      |                      |                      | react-auto           | <img src="./assets/react-auto.svg" width="48"> |
|                      |                      |                      |                      | reactivex-auto       | <img src="./assets/reactivex-auto.svg" width="48"> |
|                      |                      |                      |                      | reactquery-auto      | <img src="./assets/reactquery-auto.svg" width="48"> |
|                      |                      |                      |                      | recoil               | <img src="./assets/recoil.svg" width="48"> |
|                      |                      |                      |                      | redhat-auto          | <img src="./assets/redhat-auto.svg" width="48"> |
|                      |                      |                      |                      | redis-auto           | <img src="./assets/redis-auto.svg" width="48"> |
|                      |                      |                      |                      | redshift-auto        | <img src="./assets/redshift-auto.svg" width="48"> |
|                      |                      |                      |                      | redux                | <img src="./assets/redux.svg" width="48"> |
|                      |                      |                      |                      | regex-auto           | <img src="./assets/regex-auto.svg" width="48"> |
|                      |                      |                      |                      | remix-auto           | <img src="./assets/remix-auto.svg" width="48"> |
|                      |                      |                      |                      | replit-auto          | <img src="./assets/replit-auto.svg" width="48"> |
|                      |                      |                      |                      | resharper-auto       | <img src="./assets/resharper-auto.svg" width="48"> |
|                      |                      |                      |                      | reverb               | <img src="./assets/reverb.svg" width="48"> |
|                      |                      |                      |                      | rider-auto           | <img src="./assets/rider-auto.svg" width="48"> |
|                      |                      |                      |                      | robloxstudio         | <img src="./assets/robloxstudio.svg" width="48"> |
|                      |                      |                      |                      | rocket               | <img src="./assets/rocket.svg" width="48"> |
|                      |                      |                      |                      | rollupjs-auto        | <img src="./assets/rollupjs-auto.svg" width="48"> |
|                      |                      |                      |                      | ros-auto             | <img src="./assets/ros-auto.svg" width="48"> |
|                      |                      |                      |                      | rubocop-auto         | <img src="./assets/rubocop-auto.svg" width="48"> |
|                      |                      |                      |                      | ruby                 | <img src="./assets/ruby.svg" width="48"> |
|                      |                      |                      |                      | rubymine-auto        | <img src="./assets/rubymine-auto.svg" width="48"> |
|                      |                      |                      |                      | rust-auto            | <img src="./assets/rust-auto.svg" width="48"> |
|                      |                      |                      |                      | rustrover-auto       | <img src="./assets/rustrover-auto.svg" width="48"> |
|                      |                      |                      |                      | safari-auto          | <img src="./assets/safari-auto.svg" width="48"> |
|                      |                      |                      |                      | sail                 | <img src="./assets/sail.svg" width="48"> |
|                      |                      |                      |                      | sanctum              | <img src="./assets/sanctum.svg" width="48"> |
|                      |                      |                      |                      | sass                 | <img src="./assets/sass.svg" width="48"> |
|                      |                      |                      |                      | scala-auto           | <img src="./assets/scala-auto.svg" width="48"> |
|                      |                      |                      |                      | scikitlearn-auto     | <img src="./assets/scikitlearn-auto.svg" width="48"> |
|                      |                      |                      |                      | scipy-auto           | <img src="./assets/scipy-auto.svg" width="48"> |
|                      |                      |                      |                      | scout                | <img src="./assets/scout.svg" width="48"> |
|                      |                      |                      |                      | scratch              | <img src="./assets/scratch.svg" width="48"> |
|                      |                      |                      |                      | seaborn-auto         | <img src="./assets/seaborn-auto.svg" width="48"> |
|                      |                      |                      |                      | selenium             | <img src="./assets/selenium.svg" width="48"> |
|                      |                      |                      |                      | sentry               | <img src="./assets/sentry.svg" width="48"> |
|                      |                      |                      |                      | sequelize-auto       | <img src="./assets/sequelize-auto.svg" width="48"> |
|                      |                      |                      |                      | sharepoint-auto      | <img src="./assets/sharepoint-auto.svg" width="48"> |
|                      |                      |                      |                      | shopify-auto         | <img src="./assets/shopify-auto.svg" width="48"> |
|                      |                      |                      |                      | skeletonui-auto      | <img src="./assets/skeletonui-auto.svg" width="48"> |
|                      |                      |                      |                      | sketchup-auto        | <img src="./assets/sketchup-auto.svg" width="48"> |
|                      |                      |                      |                      | slack-auto           | <img src="./assets/slack-auto.svg" width="48"> |
|                      |                      |                      |                      | snowflake-auto       | <img src="./assets/snowflake-auto.svg" width="48"> |
|                      |                      |                      |                      | snyk-auto            | <img src="./assets/snyk-auto.svg" width="48"> |
|                      |                      |                      |                      | socialite            | <img src="./assets/socialite.svg" width="48"> |
|                      |                      |                      |                      | solidity             | <img src="./assets/solidity.svg" width="48"> |
|                      |                      |                      |                      | solidjs-auto         | <img src="./assets/solidjs-auto.svg" width="48"> |
|                      |                      |                      |                      | spark                | <img src="./assets/spark.svg" width="48"> |
|                      |                      |                      |                      | spring-auto          | <img src="./assets/spring-auto.svg" width="48"> |
|                      |                      |                      |                      | sqlite               | <img src="./assets/sqlite.svg" width="48"> |
|                      |                      |                      |                      | sqlserver-auto       | <img src="./assets/sqlserver-auto.svg" width="48"> |
|                      |                      |                      |                      | stackoverflow-auto   | <img src="./assets/stackoverflow-auto.svg" width="48"> |
|                      |                      |                      |                      | stock                | <img src="./assets/stock.svg" width="48"> |
|                      |                      |                      |                      | storyblok-auto       | <img src="./assets/storyblok-auto.svg" width="48"> |
|                      |                      |                      |                      | storybook-auto       | <img src="./assets/storybook-auto.svg" width="48"> |
|                      |                      |                      |                      | strapi               | <img src="./assets/strapi.svg" width="48"> |
|                      |                      |                      |                      | streamlit-auto       | <img src="./assets/streamlit-auto.svg" width="48"> |
|                      |                      |                      |                      | styledcomponents     | <img src="./assets/styledcomponents.svg" width="48"> |
|                      |                      |                      |                      | sublime-auto         | <img src="./assets/sublime-auto.svg" width="48"> |
|                      |                      |                      |                      | supabase-auto        | <img src="./assets/supabase-auto.svg" width="48"> |
|                      |                      |                      |                      | surrealdb-auto       | <img src="./assets/surrealdb-auto.svg" width="48"> |
|                      |                      |                      |                      | svelte               | <img src="./assets/svelte.svg" width="48"> |
|                      |                      |                      |                      | svg-auto             | <img src="./assets/svg-auto.svg" width="48"> |
|                      |                      |                      |                      | svn                  | <img src="./assets/svn.svg" width="48"> |
|                      |                      |                      |                      | swagger-auto         | <img src="./assets/swagger-auto.svg" width="48"> |
|                      |                      |                      |                      | swift                | <img src="./assets/swift.svg" width="48"> |
|                      |                      |                      |                      | symfony-auto         | <img src="./assets/symfony-auto.svg" width="48"> |
|                      |                      |                      |                      | tableau-auto         | <img src="./assets/tableau-auto.svg" width="48"> |
|                      |                      |                      |                      | tailwindcss-auto     | <img src="./assets/tailwindcss-auto.svg" width="48"> |
|                      |                      |                      |                      | tallyprime           | <img src="./assets/tallyprime.svg" width="48"> |
|                      |                      |                      |                      | tauri-auto           | <img src="./assets/tauri-auto.svg" width="48"> |
|                      |                      |                      |                      | teams-auto           | <img src="./assets/teams-auto.svg" width="48"> |
|                      |                      |                      |                      | telescope            | <img src="./assets/telescope.svg" width="48"> |
|                      |                      |                      |                      | tensorflow-auto      | <img src="./assets/tensorflow-auto.svg" width="48"> |
|                      |                      |                      |                      | terraform-auto       | <img src="./assets/terraform-auto.svg" width="48"> |
|                      |                      |                      |                      | testinglibrary-auto  | <img src="./assets/testinglibrary-auto.svg" width="48"> |
|                      |                      |                      |                      | threejs-auto         | <img src="./assets/threejs-auto.svg" width="48"> |
|                      |                      |                      |                      | tor-auto             | <img src="./assets/tor-auto.svg" width="48"> |
|                      |                      |                      |                      | trpc                 | <img src="./assets/trpc.svg" width="48"> |
|                      |                      |                      |                      | truffle-auto         | <img src="./assets/truffle-auto.svg" width="48"> |
|                      |                      |                      |                      | typescript           | <img src="./assets/typescript.svg" width="48"> |
|                      |                      |                      |                      | ubuntu               | <img src="./assets/ubuntu.svg" width="48"> |
|                      |                      |                      |                      | unity-auto           | <img src="./assets/unity-auto.svg" width="48"> |
|                      |                      |                      |                      | unrealengine         | <img src="./assets/unrealengine.svg" width="48"> |
|                      |                      |                      |                      | v-auto               | <img src="./assets/v-auto.svg" width="48"> |
|                      |                      |                      |                      | vala                 | <img src="./assets/vala.svg" width="48"> |
|                      |                      |                      |                      | vapor                | <img src="./assets/vapor.svg" width="48"> |
|                      |                      |                      |                      | vercel-auto          | <img src="./assets/vercel-auto.svg" width="48"> |
|                      |                      |                      |                      | vim-auto             | <img src="./assets/vim-auto.svg" width="48"> |
|                      |                      |                      |                      | visualbasic-auto     | <img src="./assets/visualbasic-auto.svg" width="48"> |
|                      |                      |                      |                      | visualstudio-auto    | <img src="./assets/visualstudio-auto.svg" width="48"> |
|                      |                      |                      |                      | vite-auto            | <img src="./assets/vite-auto.svg" width="48"> |
|                      |                      |                      |                      | vitest-auto          | <img src="./assets/vitest-auto.svg" width="48"> |
|                      |                      |                      |                      | vscode-auto          | <img src="./assets/vscode-auto.svg" width="48"> |
|                      |                      |                      |                      | vscodium-auto        | <img src="./assets/vscodium-auto.svg" width="48"> |
|                      |                      |                      |                      | vuejs-auto           | <img src="./assets/vuejs-auto.svg" width="48"> |
|                      |                      |                      |                      | vuetify-auto         | <img src="./assets/vuetify-auto.svg" width="48"> |
|                      |                      |                      |                      | vyper-auto           | <img src="./assets/vyper-auto.svg" width="48"> |
|                      |                      |                      |                      | webassembly          | <img src="./assets/webassembly.svg" width="48"> |
|                      |                      |                      |                      | webflow              | <img src="./assets/webflow.svg" width="48"> |
|                      |                      |                      |                      | webpack-auto         | <img src="./assets/webpack-auto.svg" width="48"> |
|                      |                      |                      |                      | webstorm-auto        | <img src="./assets/webstorm-auto.svg" width="48"> |
|                      |                      |                      |                      | windicss-auto        | <img src="./assets/windicss-auto.svg" width="48"> |
|                      |                      |                      |                      | windows-auto         | <img src="./assets/windows-auto.svg" width="48"> |
|                      |                      |                      |                      | word-auto            | <img src="./assets/word-auto.svg" width="48"> |
|                      |                      |                      |                      | wordpress            | <img src="./assets/wordpress.svg" width="48"> |
|                      |                      |                      |                      | workers-auto         | <img src="./assets/workers-auto.svg" width="48"> |
|                      |                      |                      |                      | x-auto               | <img src="./assets/x-auto.svg" width="48"> |
|                      |                      |                      |                      | xcode-auto           | <img src="./assets/xcode-auto.svg" width="48"> |
|                      |                      |                      |                      | xd                   | <img src="./assets/xd.svg" width="48"> |
|                      |                      |                      |                      | yaml-auto            | <img src="./assets/yaml-auto.svg" width="48"> |
|                      |                      |                      |                      | yammer-auto          | <img src="./assets/yammer-auto.svg" width="48"> |
|                      |                      |                      |                      | yarn-auto            | <img src="./assets/yarn-auto.svg" width="48"> |
|                      |                      |                      |                      | yew-auto             | <img src="./assets/yew-auto.svg" width="48"> |
|                      |                      |                      |                      | youtube              | <img src="./assets/youtube.svg" width="48"> |
|                      |                      |                      |                      | zed-auto             | <img src="./assets/zed-auto.svg" width="48"> |
|                      |                      |                      |                      | zig-auto             | <img src="./assets/zig-auto.svg" width="48"> |

<!-- END ICONS LIST -->
---

## 💖 Support the Project

Thank you so much already for using my projects!

To support the project directly, feel free to open issues for icon suggestions, or contribute with a pull request!
