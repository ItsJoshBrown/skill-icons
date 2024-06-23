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
<table style="text-align: left; width: 100%;">
    <tr>
        <td>Icon ID</td>
        <td>Icon</td>
        <td>Icon ID</td>
        <td>Icon</td>
        <td>Icon ID</td>
        <td>Icon</td>
        <td>Icon ID</td>
        <td>Icon</td>
    </tr>
  <tr>
    <td>ableton</td>
    <td><img src="assets/ableton-auto.svg" width="48"></td>
    <td>acrobat</td>
    <td><img src="assets/acrobat.svg" width="48"></td>
    <td>activitypub</td>
    <td><img src="assets/activitypub-auto.svg" width="48"></td>
    <td>actix</td>
    <td><img src="assets/actix-auto.svg" width="48"></td>
  </tr>
  <tr>
    <td>adonis</td>
    <td><img src="assets/adonis.svg" width="48"></td>
    <td>aero</td>
    <td><img src="assets/aero.svg" width="48"></td>
    <td>aftereffects</td>
    <td><img src="assets/aftereffects.svg" width="48"></td>
    <td>aiscript</td>
    <td><img src="assets/aiscript-auto.svg" width="48"></td>
  </tr>
  <tr>
    <td>alchemy</td>
    <td><img src="assets/alchemy-auto.svg" width="48"></td>
    <td>alpinejs</td>
    <td><img src="assets/alpinejs-auto.svg" width="48"></td>
    <td>anaconda</td>
    <td><img src="assets/anaconda-auto.svg" width="48"></td>
    <td>androidstudio</td>
    <td><img src="assets/androidstudio-auto.svg" width="48"></td>
  </tr>
  <tr>
    <td>angular</td>
    <td><img src="assets/angular-auto.svg" width="48"></td>
    <td>animate</td>
    <td><img src="assets/animate.svg" width="48"></td>
    <td>ansible</td>
    <td><img src="assets/ansible.svg" width="48"></td>
    <td>anss</td>
    <td><img src="assets/anss-auto.svg" width="48"></td>
  </tr>
  <tr>
    <td>apollo</td>
    <td><img src="assets/apollo.svg" width="48"></td>
    <td>appcode</td>
    <td><img src="assets/appcode-auto.svg" width="48"></td>
    <td>apple</td>
    <td><img src="assets/apple-auto.svg" width="48"></td>
    <td>appwrite</td>
    <td><img src="assets/appwrite.svg" width="48"></td>
  </tr>
  <tr>
    <td>aqua</td>
    <td><img src="assets/aqua-auto.svg" width="48"></td>
    <td>arch</td>
    <td><img src="assets/arch-auto.svg" width="48"></td>
    <td>arduino</td>
    <td><img src="assets/arduino.svg" width="48"></td>
    <td>argocd</td>
    <td><img src="assets/argocd-auto.svg" width="48"></td>
  </tr>
  <tr>
    <td>assembly</td>
    <td><img src="assets/assembly.svg" width="48"></td>
    <td>astro</td>
    <td><img src="assets/astro.svg" width="48"></td>
    <td>atom</td>
    <td><img src="assets/atom.svg" width="48"></td>
    <td>audition</td>
    <td><img src="assets/audition.svg" width="48"></td>
  </tr>
  <tr>
    <td>autocad</td>
    <td><img src="assets/autocad-auto.svg" width="48"></td>
    <td>aws</td>
    <td><img src="assets/aws-auto.svg" width="48"></td>
    <td>azul</td>
    <td><img src="assets/azul.svg" width="48"></td>
    <td>azure</td>
    <td><img src="assets/azure-auto.svg" width="48"></td>
  </tr>
  <tr>
    <td>babel</td>
    <td><img src="assets/babel.svg" width="48"></td>
    <td>bash</td>
    <td><img src="assets/bash-auto.svg" width="48"></td>
    <td>beeceptor</td>
    <td><img src="assets/beeceptor-auto.svg" width="48"></td>
    <td>behance</td>
    <td><img src="assets/behance.svg" width="48"></td>
  </tr>
  <tr>
    <td>bevy</td>
    <td><img src="assets/bevy-auto.svg" width="48"></td>
    <td>bitbucket</td>
    <td><img src="assets/bitbucket-auto.svg" width="48"></td>
    <td>blazor</td>
    <td><img src="assets/blazor-auto.svg" width="48"></td>
    <td>blender</td>
    <td><img src="assets/blender-auto.svg" width="48"></td>
  </tr>
  <tr>
    <td>bootstrap</td>
    <td><img src="assets/bootstrap.svg" width="48"></td>
    <td>brave</td>
    <td><img src="assets/brave-auto.svg" width="48"></td>
    <td>breeze</td>
    <td><img src="assets/breeze.svg" width="48"></td>
    <td>bridge</td>
    <td><img src="assets/bridge.svg" width="48"></td>
  </tr>
  <tr>
    <td>bsd</td>
    <td><img src="assets/bsd-auto.svg" width="48"></td>
    <td>bulma</td>
    <td><img src="assets/bulma-auto.svg" width="48"></td>
    <td>bun</td>
    <td><img src="assets/bun-auto.svg" width="48"></td>
    <td>c</td>
    <td><img src="assets/c.svg" width="48"></td>
  </tr>
  <tr>
    <td>canva</td>
    <td><img src="assets/canva-auto.svg" width="48"></td>
    <td>capacitor</td>
    <td><img src="assets/capacitor-auto.svg" width="48"></td>
    <td>capture</td>
    <td><img src="assets/capture.svg" width="48"></td>
    <td>cashier</td>
    <td><img src="assets/cashier.svg" width="48"></td>
  </tr>
  <tr>
    <td>cassandra</td>
    <td><img src="assets/cassandra-auto.svg" width="48"></td>
    <td>characteranimator</td>
    <td><img src="assets/characteranimator.svg" width="48"></td>
    <td>chatgpt</td>
    <td><img src="assets/chatgpt-auto.svg" width="48"></td>
    <td>chrome</td>
    <td><img src="assets/chrome-auto.svg" width="48"></td>
  </tr>
  <tr>
    <td>chromium</td>
    <td><img src="assets/chromium-auto.svg" width="48"></td>
    <td>circleci</td>
    <td><img src="assets/circleci-auto.svg" width="48"></td>
    <td>clion</td>
    <td><img src="assets/clion-auto.svg" width="48"></td>
    <td>clojure</td>
    <td><img src="assets/clojure-auto.svg" width="48"></td>
  </tr>
  <tr>
    <td>cloudflare</td>
    <td><img src="assets/cloudflare-auto.svg" width="48"></td>
    <td>cmake</td>
    <td><img src="assets/cmake-auto.svg" width="48"></td>
    <td>codeberg</td>
    <td><img src="assets/codeberg-auto.svg" width="48"></td>
    <td>codeigniter</td>
    <td><img src="assets/codeigniter-auto.svg" width="48"></td>
  </tr>
  <tr>
    <td>codepen</td>
    <td><img src="assets/codepen-auto.svg" width="48"></td>
    <td>coffeescript</td>
    <td><img src="assets/coffeescript-auto.svg" width="48"></td>
    <td>cpp</td>
    <td><img src="assets/cpp.svg" width="48"></td>
    <td>creativecloud</td>
    <td><img src="assets/creativecloud.svg" width="48"></td>
  </tr>
  <tr>
    <td>crystal</td>
    <td><img src="assets/crystal-auto.svg" width="48"></td>
    <td>cs</td>
    <td><img src="assets/cs.svg" width="48"></td>
    <td>css</td>
    <td><img src="assets/css.svg" width="48"></td>
    <td>cypress</td>
    <td><img src="assets/cypress-auto.svg" width="48"></td>
  </tr>
  <tr>
    <td>d</td>
    <td><img src="assets/d.svg" width="48"></td>
    <td>d3</td>
    <td><img src="assets/d3-auto.svg" width="48"></td>
    <td>dailydev</td>
    <td><img src="assets/dailydev-auto.svg" width="48"></td>
    <td>dart</td>
    <td><img src="assets/dart-auto.svg" width="48"></td>
  </tr>
  <tr>
    <td>databricks</td>
    <td><img src="assets/databricks-auto.svg" width="48"></td>
    <td>databricks-black</td>
    <td><img src="assets/databricks-black.svg" width="48"></td>
    <td>datadog</td>
    <td><img src="assets/datadog.svg" width="48"></td>
    <td>datagrip</td>
    <td><img src="assets/datagrip-auto.svg" width="48"></td>
  </tr>
  <tr>
    <td>dataspell</td>
    <td><img src="assets/dataspell-auto.svg" width="48"></td>
    <td>dbeaver</td>
    <td><img src="assets/dbeaver-auto.svg" width="48"></td>
    <td>debian</td>
    <td><img src="assets/debian.svg" width="48"></td>
    <td>defold</td>
    <td><img src="assets/defold-auto.svg" width="48"></td>
  </tr>
  <tr>
    <td>deno</td>
    <td><img src="assets/deno-auto.svg" width="48"></td>
    <td>desmos</td>
    <td><img src="assets/desmos.svg" width="48"></td>
    <td>devto</td>
    <td><img src="assets/devto-auto.svg" width="48"></td>
    <td>digitalocean</td>
    <td><img src="assets/digitalocean-dark.svg" width="48"></td>
  </tr>
  <tr>
    <td>dimension</td>
    <td><img src="assets/dimension.svg" width="48"></td>
    <td>directus</td>
    <td><img src="assets/directus.svg" width="48"></td>
    <td>discord</td>
    <td><img src="assets/discord.svg" width="48"></td>
    <td>discordbots</td>
    <td><img src="assets/discordbots.svg" width="48"></td>
  </tr>
  <tr>
    <td>discordjs</td>
    <td><img src="assets/discordjs-auto.svg" width="48"></td>
    <td>django</td>
    <td><img src="assets/django.svg" width="48"></td>
    <td>docker</td>
    <td><img src="assets/docker.svg" width="48"></td>
    <td>docksal</td>
    <td><img src="assets/docksal-auto.svg" width="48"></td>
  </tr>
  <tr>
    <td>dotnet</td>
    <td><img src="assets/dotnet.svg" width="48"></td>
    <td>dreamweaver</td>
    <td><img src="assets/dreamweaver.svg" width="48"></td>
    <td>drupal</td>
    <td><img src="assets/drupal-auto.svg" width="48"></td>
    <td>duckduckgo</td>
    <td><img src="assets/duckduckgo.svg" width="48"></td>
  </tr>
  <tr>
    <td>dusk</td>
    <td><img src="assets/dusk.svg" width="48"></td>
    <td>dynamodb</td>
    <td><img src="assets/dynamodb-auto.svg" width="48"></td>
    <td>echo</td>
    <td><img src="assets/echo.svg" width="48"></td>
    <td>eclipse</td>
    <td><img src="assets/eclipse-auto.svg" width="48"></td>
  </tr>
  <tr>
    <td>edge</td>
    <td><img src="assets/edge-auto.svg" width="48"></td>
    <td>elasticsearch</td>
    <td><img src="assets/elasticsearch-auto.svg" width="48"></td>
    <td>electron</td>
    <td><img src="assets/electron.svg" width="48"></td>
    <td>elixir</td>
    <td><img src="assets/elixir-auto.svg" width="48"></td>
  </tr>
  <tr>
    <td>elysia</td>
    <td><img src="assets/elysia-auto.svg" width="48"></td>
    <td>emacs</td>
    <td><img src="assets/emacs.svg" width="48"></td>
    <td>ember</td>
    <td><img src="assets/ember.svg" width="48"></td>
    <td>emotion</td>
    <td><img src="assets/emotion-auto.svg" width="48"></td>
  </tr>
  <tr>
    <td>envoyer</td>
    <td><img src="assets/envoyer.svg" width="48"></td>
    <td>excel</td>
    <td><img src="assets/excel-auto.svg" width="48"></td>
    <td>expressjs</td>
    <td><img src="assets/expressjs-auto.svg" width="48"></td>
    <td>facebook</td>
    <td><img src="assets/facebook.svg" width="48"></td>
  </tr>
  <tr>
    <td>fastai</td>
    <td><img src="assets/fastai-auto.svg" width="48"></td>
    <td>fastapi</td>
    <td><img src="assets/fastapi.svg" width="48"></td>
    <td>fediverse</td>
    <td><img src="assets/fediverse-auto.svg" width="48"></td>
    <td>figma</td>
    <td><img src="assets/figma-auto.svg" width="48"></td>
  </tr>
  <tr>
    <td>filament</td>
    <td><img src="assets/filament.svg" width="48"></td>
    <td>firebase</td>
    <td><img src="assets/firebase-auto.svg" width="48"></td>
    <td>firefox</td>
    <td><img src="assets/firefox-auto.svg" width="48"></td>
    <td>flameshot</td>
    <td><img src="assets/flameshot.svg" width="48"></td>
  </tr>
  <tr>
    <td>flask</td>
    <td><img src="assets/flask-auto.svg" width="48"></td>
    <td>fleet</td>
    <td><img src="assets/fleet-auto.svg" width="48"></td>
    <td>flutter</td>
    <td><img src="assets/flutter-auto.svg" width="48"></td>
    <td>fonts</td>
    <td><img src="assets/fonts.svg" width="48"></td>
  </tr>
  <tr>
    <td>forge</td>
    <td><img src="assets/forge.svg" width="48"></td>
    <td>forth</td>
    <td><img src="assets/forth.svg" width="48"></td>
    <td>fortran</td>
    <td><img src="assets/fortran.svg" width="48"></td>
    <td>fresco</td>
    <td><img src="assets/fresco.svg" width="48"></td>
  </tr>
  <tr>
    <td>fuse</td>
    <td><img src="assets/fuse.svg" width="48"></td>
    <td>gamemakerstudio</td>
    <td><img src="assets/gamemakerstudio.svg" width="48"></td>
    <td>ganache</td>
    <td><img src="assets/ganache-auto.svg" width="48"></td>
    <td>gatsby</td>
    <td><img src="assets/gatsby.svg" width="48"></td>
  </tr>
  <tr>
    <td>gcp</td>
    <td><img src="assets/gcp-auto.svg" width="48"></td>
    <td>gemini</td>
    <td><img src="assets/gemini-auto.svg" width="48"></td>
    <td>gherkin</td>
    <td><img src="assets/gherkin-auto.svg" width="48"></td>
    <td>gimp</td>
    <td><img src="assets/gimp-auto.svg" width="48"></td>
  </tr>
  <tr>
    <td>git</td>
    <td><img src="assets/git-auto.svg" width="48"></td>
    <td>github</td>
    <td><img src="assets/github-auto.svg" width="48"></td>
    <td>githubactions</td>
    <td><img src="assets/githubactions-auto.svg" width="48"></td>
    <td>githubcopilot</td>
    <td><img src="assets/githubcopilot-auto.svg" width="48"></td>
  </tr>
  <tr>
    <td>gitkraken</td>
    <td><img src="assets/gitkraken-auto.svg" width="48"></td>
    <td>gitlab</td>
    <td><img src="assets/gitlab-auto.svg" width="48"></td>
    <td>gleam</td>
    <td><img src="assets/gleam-auto.svg" width="48"></td>
    <td>gmail</td>
    <td><img src="assets/gmail-auto.svg" width="48"></td>
  </tr>
  <tr>
    <td>gnome</td>
    <td><img src="assets/gnome-auto.svg" width="48"></td>
    <td>godot</td>
    <td><img src="assets/godot-auto.svg" width="48"></td>
    <td>goland</td>
    <td><img src="assets/goland-auto.svg" width="48"></td>
    <td>golang</td>
    <td><img src="assets/golang.svg" width="48"></td>
  </tr>
  <tr>
    <td>googleanalytics</td>
    <td><img src="assets/googleanalytics-auto.svg" width="48"></td>
    <td>googleappsscript</td>
    <td><img src="assets/googleappsscript-auto.svg" width="48"></td>
    <td>gradle</td>
    <td><img src="assets/gradle-auto.svg" width="48"></td>
    <td>grafana</td>
    <td><img src="assets/grafana-auto.svg" width="48"></td>
  </tr>
  <tr>
    <td>grails</td>
    <td><img src="assets/grails.svg" width="48"></td>
    <td>graphql</td>
    <td><img src="assets/graphql-auto.svg" width="48"></td>
    <td>grunt</td>
    <td><img src="assets/grunt-auto.svg" width="48"></td>
    <td>gsap</td>
    <td><img src="assets/gsap-auto.svg" width="48"></td>
  </tr>
  <tr>
    <td>gtk</td>
    <td><img src="assets/gtk-auto.svg" width="48"></td>
    <td>gulp</td>
    <td><img src="assets/gulp.svg" width="48"></td>
    <td>hardhat</td>
    <td><img src="assets/hardhat-auto.svg" width="48"></td>
    <td>haskell</td>
    <td><img src="assets/haskell-auto.svg" width="48"></td>
  </tr>
  <tr>
    <td>haxe</td>
    <td><img src="assets/haxe-auto.svg" width="48"></td>
    <td>haxeflixel</td>
    <td><img src="assets/haxeflixel-auto.svg" width="48"></td>
    <td>helix</td>
    <td><img src="assets/helix-auto.svg" width="48"></td>
    <td>helm</td>
    <td><img src="assets/helm-auto.svg" width="48"></td>
  </tr>
  <tr>
    <td>herd</td>
    <td><img src="assets/herd.svg" width="48"></td>
    <td>heroku</td>
    <td><img src="assets/heroku.svg" width="48"></td>
    <td>hibernate</td>
    <td><img src="assets/hibernate-auto.svg" width="48"></td>
    <td>holyc</td>
    <td><img src="assets/holyc.svg" width="48"></td>
  </tr>
  <tr>
    <td>hono</td>
    <td><img src="assets/hono-auto.svg" width="48"></td>
    <td>horizon</td>
    <td><img src="assets/horizon.svg" width="48"></td>
    <td>html</td>
    <td><img src="assets/html.svg" width="48"></td>
    <td>htmx</td>
    <td><img src="assets/htmx-auto.svg" width="48"></td>
  </tr>
  <tr>
    <td>htop</td>
    <td><img src="assets/htop-auto.svg" width="48"></td>
    <td>hydrogen</td>
    <td><img src="assets/hydrogen-auto.svg" width="48"></td>
    <td>hyprland</td>
    <td><img src="assets/hyprland-auto.svg" width="48"></td>
    <td>i3</td>
    <td><img src="assets/i3-auto.svg" width="48"></td>
  </tr>
  <tr>
    <td>idea</td>
    <td><img src="assets/idea-auto.svg" width="48"></td>
    <td>ignite</td>
    <td><img src="assets/ignite-auto.svg" width="48"></td>
    <td>illustrator</td>
    <td><img src="assets/illustrator.svg" width="48"></td>
    <td>incopy</td>
    <td><img src="assets/incopy.svg" width="48"></td>
  </tr>
  <tr>
    <td>indesign</td>
    <td><img src="assets/indesign.svg" width="48"></td>
    <td>inertia</td>
    <td><img src="assets/inertia.svg" width="48"></td>
    <td>infura</td>
    <td><img src="assets/infura.svg" width="48"></td>
    <td>insomnia</td>
    <td><img src="assets/insomnia.svg" width="48"></td>
  </tr>
  <tr>
    <td>instagram</td>
    <td><img src="assets/instagram.svg" width="48"></td>
    <td>ipfs</td>
    <td><img src="assets/ipfs-auto.svg" width="48"></td>
    <td>java</td>
    <td><img src="assets/java-auto.svg" width="48"></td>
    <td>javascript</td>
    <td><img src="assets/javascript.svg" width="48"></td>
  </tr>
  <tr>
    <td>jenkins</td>
    <td><img src="assets/jenkins-auto.svg" width="48"></td>
    <td>jest</td>
    <td><img src="assets/jest.svg" width="48"></td>
    <td>jetpackcompose</td>
    <td><img src="assets/jetpackcompose-auto.svg" width="48"></td>
    <td>jetstream</td>
    <td><img src="assets/jetstream.svg" width="48"></td>
  </tr>
  <tr>
    <td>jira</td>
    <td><img src="assets/jira-auto.svg" width="48"></td>
    <td>joomla</td>
    <td><img src="assets/joomla-auto.svg" width="48"></td>
    <td>jquery</td>
    <td><img src="assets/jquery.svg" width="48"></td>
    <td>julia</td>
    <td><img src="assets/julia-auto.svg" width="48"></td>
  </tr>
  <tr>
    <td>kafka</td>
    <td><img src="assets/kafka.svg" width="48"></td>
    <td>kaggle</td>
    <td><img src="assets/kaggle-auto.svg" width="48"></td>
    <td>kakoune</td>
    <td><img src="assets/kakoune-auto.svg" width="48"></td>
    <td>kali</td>
    <td><img src="assets/kali-auto.svg" width="48"></td>
  </tr>
  <tr>
    <td>kde</td>
    <td><img src="assets/kde-auto.svg" width="48"></td>
    <td>keycloak</td>
    <td><img src="assets/keycloak.svg" width="48"></td>
    <td>kotlin</td>
    <td><img src="assets/kotlin-auto.svg" width="48"></td>
    <td>ktor</td>
    <td><img src="assets/ktor-auto.svg" width="48"></td>
  </tr>
  <tr>
    <td>kubernetes</td>
    <td><img src="assets/kubernetes.svg" width="48"></td>
    <td>langchain</td>
    <td><img src="assets/langchain-auto.svg" width="48"></td>
    <td>laravel</td>
    <td><img src="assets/laravel-auto.svg" width="48"></td>
    <td>laravelspark</td>
    <td><img src="assets/laravelspark-auto.svg" width="48"></td>
  </tr>
  <tr>
    <td>latex</td>
    <td><img src="assets/latex-auto.svg" width="48"></td>
    <td>leetcode</td>
    <td><img src="assets/leetcode-auto.svg" width="48"></td>
    <td>less</td>
    <td><img src="assets/less-auto.svg" width="48"></td>
    <td>lightning</td>
    <td><img src="assets/lightning-auto.svg" width="48"></td>
  </tr>
  <tr>
    <td>lightroom</td>
    <td><img src="assets/lightroom.svg" width="48"></td>
    <td>lightroomclassic</td>
    <td><img src="assets/lightroomclassic.svg" width="48"></td>
    <td>linkedin</td>
    <td><img src="assets/linkedin.svg" width="48"></td>
    <td>linux</td>
    <td><img src="assets/linux-auto.svg" width="48"></td>
  </tr>
  <tr>
    <td>lit</td>
    <td><img src="assets/lit-auto.svg" width="48"></td>
    <td>litmus</td>
    <td><img src="assets/litmus-auto.svg" width="48"></td>
    <td>livewire</td>
    <td><img src="assets/livewire-auto.svg" width="48"></td>
    <td>looker</td>
    <td><img src="assets/looker-auto.svg" width="48"></td>
  </tr>
  <tr>
    <td>lua</td>
    <td><img src="assets/lua-auto.svg" width="48"></td>
    <td>lucidchart</td>
    <td><img src="assets/lucidchart-auto.svg" width="48"></td>
    <td>manjaro</td>
    <td><img src="assets/manjaro.svg" width="48"></td>
    <td>markdown</td>
    <td><img src="assets/markdown-auto.svg" width="48"></td>
  </tr>
  <tr>
    <td>mastodon</td>
    <td><img src="assets/mastodon-auto.svg" width="48"></td>
    <td>materialui</td>
    <td><img src="assets/materialui-auto.svg" width="48"></td>
    <td>matlab</td>
    <td><img src="assets/matlab-auto.svg" width="48"></td>
    <td>matplotlib</td>
    <td><img src="assets/matplotlib-auto.svg" width="48"></td>
  </tr>
  <tr>
    <td>maven</td>
    <td><img src="assets/maven-auto.svg" width="48"></td>
    <td>mediaencoder</td>
    <td><img src="assets/mediaencoder.svg" width="48"></td>
    <td>mermaid</td>
    <td><img src="assets/mermaid.svg" width="48"></td>
    <td>meteorjs</td>
    <td><img src="assets/meteorjs-auto.svg" width="48"></td>
  </tr>
  <tr>
    <td>microsoftcopilot</td>
    <td><img src="assets/microsoftcopilot-auto.svg" width="48"></td>
    <td>millionjs</td>
    <td><img src="assets/millionjs-auto.svg" width="48"></td>
    <td>mint</td>
    <td><img src="assets/mint-auto.svg" width="48"></td>
    <td>miro</td>
    <td><img src="assets/miro.svg" width="48"></td>
  </tr>
  <tr>
    <td>misskey</td>
    <td><img src="assets/misskey-auto.svg" width="48"></td>
    <td>mjml</td>
    <td><img src="assets/mjml-auto.svg" width="48"></td>
    <td>ml5</td>
    <td><img src="assets/ml5-auto.svg" width="48"></td>
    <td>mojo</td>
    <td><img src="assets/mojo-auto.svg" width="48"></td>
  </tr>
  <tr>
    <td>mongodb</td>
    <td><img src="assets/mongodb.svg" width="48"></td>
    <td>mysql</td>
    <td><img src="assets/mysql-auto.svg" width="48"></td>
    <td>neovim</td>
    <td><img src="assets/neovim-auto.svg" width="48"></td>
    <td>nestjs</td>
    <td><img src="assets/nestjs-auto.svg" width="48"></td>
  </tr>
  <tr>
    <td>netlify</td>
    <td><img src="assets/netlify-auto.svg" width="48"></td>
    <td>nextjs</td>
    <td><img src="assets/nextjs-auto.svg" width="48"></td>
    <td>nginx</td>
    <td><img src="assets/nginx.svg" width="48"></td>
    <td>ngrok</td>
    <td><img src="assets/ngrok.svg" width="48"></td>
  </tr>
  <tr>
    <td>nim</td>
    <td><img src="assets/nim-auto.svg" width="48"></td>
    <td>nixos</td>
    <td><img src="assets/nixos-auto.svg" width="48"></td>
    <td>nodejs</td>
    <td><img src="assets/nodejs-auto.svg" width="48"></td>
    <td>notion</td>
    <td><img src="assets/notion-auto.svg" width="48"></td>
  </tr>
  <tr>
    <td>nova</td>
    <td><img src="assets/nova.svg" width="48"></td>
    <td>npm</td>
    <td><img src="assets/npm-auto.svg" width="48"></td>
    <td>numpy</td>
    <td><img src="assets/numpy-auto.svg" width="48"></td>
    <td>nuxtjs</td>
    <td><img src="assets/nuxtjs-auto.svg" width="48"></td>
  </tr>
  <tr>
    <td>obsidian</td>
    <td><img src="assets/obsidian-auto.svg" width="48"></td>
    <td>ocaml</td>
    <td><img src="assets/ocaml.svg" width="48"></td>
    <td>octane</td>
    <td><img src="assets/octane.svg" width="48"></td>
    <td>octave</td>
    <td><img src="assets/octave-auto.svg" width="48"></td>
  </tr>
  <tr>
    <td>ollama</td>
    <td><img src="assets/ollama-auto.svg" width="48"></td>
    <td>onedrive</td>
    <td><img src="assets/onedrive-auto.svg" width="48"></td>
    <td>onenote</td>
    <td><img src="assets/onenote-auto.svg" width="48"></td>
    <td>opencv</td>
    <td><img src="assets/opencv-auto.svg" width="48"></td>
  </tr>
  <tr>
    <td>openshift</td>
    <td><img src="assets/openshift.svg" width="48"></td>
    <td>openstack</td>
    <td><img src="assets/openstack-auto.svg" width="48"></td>
    <td>openzeppelin</td>
    <td><img src="assets/openzeppelin-auto.svg" width="48"></td>
    <td>opera</td>
    <td><img src="assets/opera-auto.svg" width="48"></td>
  </tr>
  <tr>
    <td>oracle</td>
    <td><img src="assets/oracle-auto.svg" width="48"></td>
    <td>outlook</td>
    <td><img src="assets/outlook-auto.svg" width="48"></td>
    <td>p5js</td>
    <td><img src="assets/p5js.svg" width="48"></td>
    <td>pail</td>
    <td><img src="assets/pail-auto.svg" width="48"></td>
  </tr>
  <tr>
    <td>pandas</td>
    <td><img src="assets/pandas-auto.svg" width="48"></td>
    <td>papertrail</td>
    <td><img src="assets/papertrail.svg" width="48"></td>
    <td>payload</td>
    <td><img src="assets/payload-auto.svg" width="48"></td>
    <td>pbi</td>
    <td><img src="assets/pbi-auto.svg" width="48"></td>
  </tr>
  <tr>
    <td>pennant</td>
    <td><img src="assets/pennant.svg" width="48"></td>
    <td>perl</td>
    <td><img src="assets/perl.svg" width="48"></td>
    <td>photoshop</td>
    <td><img src="assets/photoshop.svg" width="48"></td>
    <td>photoshopclassic</td>
    <td><img src="assets/photoshopclassic.svg" width="48"></td>
  </tr>
  <tr>
    <td>photoshopexpress</td>
    <td><img src="assets/photoshopexpress.svg" width="48"></td>
    <td>php</td>
    <td><img src="assets/php-auto.svg" width="48"></td>
    <td>phpstorm</td>
    <td><img src="assets/phpstorm-auto.svg" width="48"></td>
    <td>picocss</td>
    <td><img src="assets/picocss-auto.svg" width="48"></td>
  </tr>
  <tr>
    <td>pinecone</td>
    <td><img src="assets/pinecone-auto.svg" width="48"></td>
    <td>pinia</td>
    <td><img src="assets/pinia-auto.svg" width="48"></td>
    <td>pint</td>
    <td><img src="assets/pint.svg" width="48"></td>
    <td>pkl</td>
    <td><img src="assets/pkl-auto.svg" width="48"></td>
  </tr>
  <tr>
    <td>plan9</td>
    <td><img src="assets/plan9-auto.svg" width="48"></td>
    <td>planetscale</td>
    <td><img src="assets/planetscale-auto.svg" width="48"></td>
    <td>playwright</td>
    <td><img src="assets/playwright-auto.svg" width="48"></td>
    <td>pnpm</td>
    <td><img src="assets/pnpm-auto.svg" width="48"></td>
  </tr>
  <tr>
    <td>pocketbase</td>
    <td><img src="assets/pocketbase-auto.svg" width="48"></td>
    <td>popos</td>
    <td><img src="assets/popos.svg" width="48"></td>
    <td>portfolio</td>
    <td><img src="assets/portfolio.svg" width="48"></td>
    <td>postgresql</td>
    <td><img src="assets/postgresql-auto.svg" width="48"></td>
  </tr>
  <tr>
    <td>postman</td>
    <td><img src="assets/postman.svg" width="48"></td>
    <td>powerpoint</td>
    <td><img src="assets/powerpoint-auto.svg" width="48"></td>
    <td>powershell</td>
    <td><img src="assets/powershell-auto.svg" width="48"></td>
    <td>preact</td>
    <td><img src="assets/preact-auto.svg" width="48"></td>
  </tr>
  <tr>
    <td>prelude</td>
    <td><img src="assets/prelude.svg" width="48"></td>
    <td>premiere</td>
    <td><img src="assets/premiere.svg" width="48"></td>
    <td>premiererush</td>
    <td><img src="assets/premiererush.svg" width="48"></td>
    <td>prisma</td>
    <td><img src="assets/prisma.svg" width="48"></td>
  </tr>
  <tr>
    <td>processing</td>
    <td><img src="assets/processing-auto.svg" width="48"></td>
    <td>prometheus</td>
    <td><img src="assets/prometheus.svg" width="48"></td>
    <td>prompts</td>
    <td><img src="assets/prompts.svg" width="48"></td>
    <td>proton</td>
    <td><img src="assets/proton-auto.svg" width="48"></td>
  </tr>
  <tr>
    <td>proxmox</td>
    <td><img src="assets/proxmox-auto.svg" width="48"></td>
    <td>pug</td>
    <td><img src="assets/pug-auto.svg" width="48"></td>
    <td>pulse</td>
    <td><img src="assets/pulse-auto.svg" width="48"></td>
    <td>puppeteer</td>
    <td><img src="assets/puppeteer-auto.svg" width="48"></td>
  </tr>
  <tr>
    <td>pycharm</td>
    <td><img src="assets/pycharm-auto.svg" width="48"></td>
    <td>python</td>
    <td><img src="assets/python-auto.svg" width="48"></td>
    <td>pytorch</td>
    <td><img src="assets/pytorch-auto.svg" width="48"></td>
    <td>pyxel</td>
    <td><img src="assets/pyxel-auto.svg" width="48"></td>
  </tr>
  <tr>
    <td>qodana</td>
    <td><img src="assets/qodana-auto.svg" width="48"></td>
    <td>qt</td>
    <td><img src="assets/qt-auto.svg" width="48"></td>
    <td>r</td>
    <td><img src="assets/r-auto.svg" width="48"></td>
    <td>rabbitmq</td>
    <td><img src="assets/rabbitmq-auto.svg" width="48"></td>
  </tr>
  <tr>
    <td>rails</td>
    <td><img src="assets/rails.svg" width="48"></td>
    <td>raspberrypi</td>
    <td><img src="assets/raspberrypi-auto.svg" width="48"></td>
    <td>react</td>
    <td><img src="assets/react-auto.svg" width="48"></td>
    <td>reactivex</td>
    <td><img src="assets/reactivex-auto.svg" width="48"></td>
  </tr>
  <tr>
    <td>reactquery</td>
    <td><img src="assets/reactquery-auto.svg" width="48"></td>
    <td>recoil</td>
    <td><img src="assets/recoil.svg" width="48"></td>
    <td>redhat</td>
    <td><img src="assets/redhat-auto.svg" width="48"></td>
    <td>redis</td>
    <td><img src="assets/redis-auto.svg" width="48"></td>
  </tr>
  <tr>
    <td>redshift</td>
    <td><img src="assets/redshift-auto.svg" width="48"></td>
    <td>redux</td>
    <td><img src="assets/redux.svg" width="48"></td>
    <td>regex</td>
    <td><img src="assets/regex-auto.svg" width="48"></td>
    <td>remix</td>
    <td><img src="assets/remix-auto.svg" width="48"></td>
  </tr>
  <tr>
    <td>replit</td>
    <td><img src="assets/replit-auto.svg" width="48"></td>
    <td>resharper</td>
    <td><img src="assets/resharper-auto.svg" width="48"></td>
    <td>reverb</td>
    <td><img src="assets/reverb.svg" width="48"></td>
    <td>rider</td>
    <td><img src="assets/rider-auto.svg" width="48"></td>
  </tr>
  <tr>
    <td>robloxstudio</td>
    <td><img src="assets/robloxstudio.svg" width="48"></td>
    <td>rocket</td>
    <td><img src="assets/rocket.svg" width="48"></td>
    <td>rollupjs</td>
    <td><img src="assets/rollupjs-auto.svg" width="48"></td>
    <td>ros</td>
    <td><img src="assets/ros-auto.svg" width="48"></td>
  </tr>
  <tr>
    <td>rubocop</td>
    <td><img src="assets/rubocop-auto.svg" width="48"></td>
    <td>ruby</td>
    <td><img src="assets/ruby.svg" width="48"></td>
    <td>rubymine</td>
    <td><img src="assets/rubymine-auto.svg" width="48"></td>
    <td>rust</td>
    <td><img src="assets/rust-auto.svg" width="48"></td>
  </tr>
  <tr>
    <td>rustrover</td>
    <td><img src="assets/rustrover-auto.svg" width="48"></td>
    <td>safari</td>
    <td><img src="assets/safari-auto.svg" width="48"></td>
    <td>sail</td>
    <td><img src="assets/sail.svg" width="48"></td>
    <td>sanctum</td>
    <td><img src="assets/sanctum.svg" width="48"></td>
  </tr>
  <tr>
    <td>sass</td>
    <td><img src="assets/sass.svg" width="48"></td>
    <td>scala</td>
    <td><img src="assets/scala-auto.svg" width="48"></td>
    <td>scikitlearn</td>
    <td><img src="assets/scikitlearn-auto.svg" width="48"></td>
    <td>scipy</td>
    <td><img src="assets/scipy-auto.svg" width="48"></td>
  </tr>
  <tr>
    <td>scout</td>
    <td><img src="assets/scout.svg" width="48"></td>
    <td>scratch</td>
    <td><img src="assets/scratch.svg" width="48"></td>
    <td>seaborn</td>
    <td><img src="assets/seaborn-auto.svg" width="48"></td>
    <td>selenium</td>
    <td><img src="assets/selenium.svg" width="48"></td>
  </tr>
  <tr>
    <td>sentry</td>
    <td><img src="assets/sentry.svg" width="48"></td>
    <td>sequelize</td>
    <td><img src="assets/sequelize-auto.svg" width="48"></td>
    <td>sharepoint</td>
    <td><img src="assets/sharepoint-auto.svg" width="48"></td>
    <td>shopify</td>
    <td><img src="assets/shopify-auto.svg" width="48"></td>
  </tr>
  <tr>
    <td>skeletonui</td>
    <td><img src="assets/skeletonui-auto.svg" width="48"></td>
    <td>sketchup</td>
    <td><img src="assets/sketchup-auto.svg" width="48"></td>
    <td>slack</td>
    <td><img src="assets/slack-auto.svg" width="48"></td>
    <td>snowflake</td>
    <td><img src="assets/snowflake-auto.svg" width="48"></td>
  </tr>
  <tr>
    <td>snyk</td>
    <td><img src="assets/snyk-auto.svg" width="48"></td>
    <td>socialite</td>
    <td><img src="assets/socialite.svg" width="48"></td>
    <td>solidity</td>
    <td><img src="assets/solidity.svg" width="48"></td>
    <td>solidjs</td>
    <td><img src="assets/solidjs-auto.svg" width="48"></td>
  </tr>
  <tr>
    <td>spark</td>
    <td><img src="assets/spark.svg" width="48"></td>
    <td>spring</td>
    <td><img src="assets/spring-auto.svg" width="48"></td>
    <td>sqlite</td>
    <td><img src="assets/sqlite.svg" width="48"></td>
    <td>sqlserver</td>
    <td><img src="assets/sqlserver-auto.svg" width="48"></td>
  </tr>
  <tr>
    <td>stackoverflow</td>
    <td><img src="assets/stackoverflow-auto.svg" width="48"></td>
    <td>stock</td>
    <td><img src="assets/stock.svg" width="48"></td>
    <td>storyblok</td>
    <td><img src="assets/storyblok-auto.svg" width="48"></td>
    <td>storybook</td>
    <td><img src="assets/storybook-auto.svg" width="48"></td>
  </tr>
  <tr>
    <td>strapi</td>
    <td><img src="assets/strapi.svg" width="48"></td>
    <td>streamlit</td>
    <td><img src="assets/streamlit-auto.svg" width="48"></td>
    <td>styledcomponents</td>
    <td><img src="assets/styledcomponents.svg" width="48"></td>
    <td>sublime</td>
    <td><img src="assets/sublime-auto.svg" width="48"></td>
  </tr>
  <tr>
    <td>supabase</td>
    <td><img src="assets/supabase-auto.svg" width="48"></td>
    <td>surrealdb</td>
    <td><img src="assets/surrealdb-auto.svg" width="48"></td>
    <td>svelte</td>
    <td><img src="assets/svelte.svg" width="48"></td>
    <td>svg</td>
    <td><img src="assets/svg-auto.svg" width="48"></td>
  </tr>
  <tr>
    <td>svn</td>
    <td><img src="assets/svn.svg" width="48"></td>
    <td>swagger</td>
    <td><img src="assets/swagger-auto.svg" width="48"></td>
    <td>swift</td>
    <td><img src="assets/swift.svg" width="48"></td>
    <td>symfony</td>
    <td><img src="assets/symfony-auto.svg" width="48"></td>
  </tr>
  <tr>
    <td>tableau</td>
    <td><img src="assets/tableau-auto.svg" width="48"></td>
    <td>tailwindcss</td>
    <td><img src="assets/tailwindcss-auto.svg" width="48"></td>
    <td>tallyprime</td>
    <td><img src="assets/tallyprime.svg" width="48"></td>
    <td>tauri</td>
    <td><img src="assets/tauri-auto.svg" width="48"></td>
  </tr>
  <tr>
    <td>teams</td>
    <td><img src="assets/teams-auto.svg" width="48"></td>
    <td>telescope</td>
    <td><img src="assets/telescope.svg" width="48"></td>
    <td>tensorflow</td>
    <td><img src="assets/tensorflow-auto.svg" width="48"></td>
    <td>terraform</td>
    <td><img src="assets/terraform-auto.svg" width="48"></td>
  </tr>
  <tr>
    <td>testinglibrary</td>
    <td><img src="assets/testinglibrary-auto.svg" width="48"></td>
    <td>threejs</td>
    <td><img src="assets/threejs-auto.svg" width="48"></td>
    <td>tor</td>
    <td><img src="assets/tor-auto.svg" width="48"></td>
    <td>trpc</td>
    <td><img src="assets/trpc.svg" width="48"></td>
  </tr>
  <tr>
    <td>truffle</td>
    <td><img src="assets/truffle-auto.svg" width="48"></td>
    <td>typescript</td>
    <td><img src="assets/typescript.svg" width="48"></td>
    <td>ubuntu</td>
    <td><img src="assets/ubuntu.svg" width="48"></td>
    <td>unity</td>
    <td><img src="assets/unity-auto.svg" width="48"></td>
  </tr>
  <tr>
    <td>unrealengine</td>
    <td><img src="assets/unrealengine.svg" width="48"></td>
    <td>v</td>
    <td><img src="assets/v-auto.svg" width="48"></td>
    <td>vala</td>
    <td><img src="assets/vala.svg" width="48"></td>
    <td>vapor</td>
    <td><img src="assets/vapor.svg" width="48"></td>
  </tr>
  <tr>
    <td>vercel</td>
    <td><img src="assets/vercel-auto.svg" width="48"></td>
    <td>vim</td>
    <td><img src="assets/vim-auto.svg" width="48"></td>
    <td>visualbasic</td>
    <td><img src="assets/visualbasic-auto.svg" width="48"></td>
    <td>visualstudio</td>
    <td><img src="assets/visualstudio-auto.svg" width="48"></td>
  </tr>
  <tr>
    <td>vite</td>
    <td><img src="assets/vite-auto.svg" width="48"></td>
    <td>vitest</td>
    <td><img src="assets/vitest-auto.svg" width="48"></td>
    <td>vscode</td>
    <td><img src="assets/vscode-auto.svg" width="48"></td>
    <td>vscodium</td>
    <td><img src="assets/vscodium-auto.svg" width="48"></td>
  </tr>
  <tr>
    <td>vuejs</td>
    <td><img src="assets/vuejs-auto.svg" width="48"></td>
    <td>vuetify</td>
    <td><img src="assets/vuetify-auto.svg" width="48"></td>
    <td>vyper</td>
    <td><img src="assets/vyper-auto.svg" width="48"></td>
    <td>webassembly</td>
    <td><img src="assets/webassembly.svg" width="48"></td>
  </tr>
  <tr>
    <td>webflow</td>
    <td><img src="assets/webflow.svg" width="48"></td>
    <td>webpack</td>
    <td><img src="assets/webpack-auto.svg" width="48"></td>
    <td>webstorm</td>
    <td><img src="assets/webstorm-auto.svg" width="48"></td>
    <td>windicss</td>
    <td><img src="assets/windicss-auto.svg" width="48"></td>
  </tr>
  <tr>
    <td>windows</td>
    <td><img src="assets/windows-auto.svg" width="48"></td>
    <td>word</td>
    <td><img src="assets/word-auto.svg" width="48"></td>
    <td>wordpress</td>
    <td><img src="assets/wordpress.svg" width="48"></td>
    <td>workers</td>
    <td><img src="assets/workers-auto.svg" width="48"></td>
  </tr>
  <tr>
    <td>x</td>
    <td><img src="assets/x-auto.svg" width="48"></td>
    <td>xcode</td>
    <td><img src="assets/xcode-auto.svg" width="48"></td>
    <td>xd</td>
    <td><img src="assets/xd.svg" width="48"></td>
    <td>yaml</td>
    <td><img src="assets/yaml-auto.svg" width="48"></td>
  </tr>
  <tr>
    <td>yammer</td>
    <td><img src="assets/yammer-auto.svg" width="48"></td>
    <td>yarn</td>
    <td><img src="assets/yarn-auto.svg" width="48"></td>
    <td>yew</td>
    <td><img src="assets/yew-auto.svg" width="48"></td>
    <td>youtube</td>
    <td><img src="assets/youtube.svg" width="48"></td>
  </tr>
  <tr>
    <td>zed</td>
    <td><img src="assets/zed-auto.svg" width="48"></td>
    <td>zig</td>
    <td><img src="assets/zig-auto.svg" width="48"></td>
  </tr>
</table>

<!-- END ICONS LIST -->
---

## 💖 Support the Project

Thank you so much already for using my projects!

To support the project directly, feel free to open issues for icon suggestions, or contribute with a pull request!
