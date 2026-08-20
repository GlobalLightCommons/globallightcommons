---
layout: default
title: Resources
page_css: /assets/css/resources.css
---

<main class="resources-page">

  <section class="resources-intro">
    <h1>Resources</h1>

    <p>
      Explore our research publications, software tools, and related initiatives
      in the field of light exposure and health.
    </p>
  </section>


  <section class="resources-content">

    <nav class="resources-tabs" aria-label="Resource categories">
      <a href="#preprints">Preprints</a>
      <a href="#articles">Research Articles</a>
      <a href="#software">Software</a>
      <a href="#projects">Related Projects</a>
    </nav>


    <section class="resources-group" id="preprints">
      <h2>Preprints</h2>

      <div class="resources-list">
        {% bibliography --query @*[resource_type=preprint] %}
      </div>
    </section>


    <section class="resources-group" id="articles">
      <h2>Research Articles</h2>

      <div class="resources-list">
        {% bibliography --query @*[resource_type=article] %}
      </div>
    </section>


    <section class="resources-group" id="software">
      <h2>Software</h2>

      <div class="resources-list">
        {% bibliography --query @*[resource_type=software] %}
      </div>
    </section>


    <section class="resources-group" id="projects">
      <h2>Related Projects</h2>

      <div class="resources-list">
        {% bibliography --query @*[resource_type=project] %}
      </div>
    </section>

  </section>

</main>