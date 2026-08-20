---
layout: default
title: News & Events
page_css: /assets/css/events.css
---

<main class="events-page">

  <section class="events-intro">
    <h1>News & Events</h1>

    <p>
      Stay updated with the latest news, events, and workshops from the GLC
      research initiative.
    </p>
  </section>


  {% assign upcoming_events = site.events
    | where: "event_type", "upcoming"
  %}

  {% if upcoming_events.size > 0 %}
    <section class="events-upcoming">

      <p class="events-kicker">
        Upcoming Event Series
      </p>

      {% for event in upcoming_events %}

        <article class="featured-event">

          {% if event.image %}
            <div class="featured-event-image">
              <img
                src="{{ event.image | relative_url }}"
                alt="{{ event.title }}"
              >
            </div>
          {% endif %}


          <div class="featured-event-body">

            <h2>{{ event.title }}</h2>

            {% if event.subtitle %}
              <p class="featured-event-subtitle">
                {{ event.subtitle }}
              </p>
            {% endif %}


            <div class="featured-event-intro">

              {% if event.intro %}
                <p>{{ event.intro }}</p>
              {% endif %}

              {% if event.audience %}
                <p>
                  <strong>{{ event.audience }}</strong>
                </p>
              {% endif %}

              {% if event.description %}
                <p>{{ event.description }}</p>
              {% endif %}

            </div>


            <div class="training-tracks">

              <article class="training-card training-card-beginner">

                <p class="training-label">Beginner</p>

                <h3>Beginner Course</h3>

                <p>
                  <strong>Part 1:</strong>
                  {{ event.beginner_part_1 }}
                  <br>

                  <strong>Part 2:</strong>
                  {{ event.beginner_part_2 }}
                </p>

                <p>
                  <strong>Topics:</strong>
                  {{ event.beginner_topics }}
                </p>

              </article>


              <article class="training-card training-card-advanced">

                <p class="training-label">Advanced</p>

                <h3>Advanced Course</h3>

                <p>
                  <strong>Part 1:</strong>
                  {{ event.advanced_part_1 }}
                  <br>

                  <strong>Part 2:</strong>
                  {{ event.advanced_part_2 }}
                </p>

                <p>
                  <strong>Topics:</strong>
                  {{ event.advanced_topics }}
                </p>

              </article>

            </div>


            <div class="event-format">

              <h3>Format</h3>

              {% if event.format %}
                <p>{{ event.format }}</p>
              {% endif %}

              {% if event.schedule %}
                <p>
                  <strong>{{ event.schedule }}</strong>
                  {% if event.schedule_note %}
                    <br>
                    {{ event.schedule_note }}
                  {% endif %}
                </p>
              {% endif %}

              {% if event.qa %}
                <p>{{ event.qa }}</p>
              {% endif %}

              {% if event.certificate %}
                <p>
                  <strong>{{ event.certificate }}</strong>
                </p>
              {% endif %}

            </div>


            <div class="featured-event-actions">

              {% if event.registration_url != blank %}
                <a
                  class="event-button"
                  href="{{ event.registration_url }}"
                  target="_blank"
                  rel="noopener noreferrer"
                >
                  Register Now
                </a>
              {% endif %}

              {% if event.lightlogr_url %}
                <a
                  class="event-button event-button-secondary"
                  href="{{ event.lightlogr_url }}"
                  target="_blank"
                  rel="noopener noreferrer"
                >
                  Learn More About LightLogR →
                </a>
              {% endif %}

            </div>

          </div>
        </article>

      {% endfor %}

    </section>
  {% endif %}


  <section class="past-events">

    <h2>Past Events</h2>

    {% assign past_events = site.events
      | where: "event_type", "past"
      | sort: "date"
      | reverse
    %}

    <div class="past-events-list">

      {% for event in past_events %}

        <article class="past-event">

          {% if event.image %}
            <div class="past-event-image">

              <img
                src="{{ event.image | relative_url }}"
                alt="{{ event.title }}"
              >

            </div>
          {% endif %}


          <div class="past-event-body">

            <p class="past-event-date">
              {{ event.date | date: "%B %d, %Y" }}
            </p>

            <h3>{{ event.title }}</h3>

            {% if event.description %}
              <p>{{ event.description }}</p>
            {% endif %}

            {% if event.description_2 %}
              <p>{{ event.description_2 }}</p>
            {% endif %}


            {% if event.location or event.participants %}
              <div class="event-meta">

                {% if event.location %}
                  <span>{{ event.location }}</span>
                {% endif %}

                {% if event.participants %}
                  <span>{{ event.participants }}</span>
                {% endif %}

              </div>
            {% endif %}


            {% if event.external_url != blank %}
              <a
                class="event-link"
                href="{{ event.external_url }}"
                target="_blank"
                rel="noopener noreferrer"
              >
                {{ event.link_text }} →
              </a>
            {% elsif event.link_text %}
              <span class="event-link event-link-disabled">
                {{ event.link_text }}
              </span>
            {% endif %}

          </div>

        </article>

      {% endfor %}

    </div>

  </section>

</main>