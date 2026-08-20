---
layout: default
title: Contact Us
page_css: /assets/css/contact.css
---

<main class="contact-page">

  <section class="contact-intro">
    <h1>Contact Us</h1>

    <p>
      Get in touch with the GLC research team or join our mailing list to stay updated on our
      latest work.
    </p>
  </section>


  <section class="contact-layout">

    <div class="contact-main">

      <div class="contact-form-card">
        <h2>Keep up to date!</h2>

        <p class="contact-form-intro">
          Join our mailing list to receive updates on the latest developments, upcoming webinars,
          and collaborative opportunities in visual experience and optical radiation research.
          Be part of a global community dedicated to advancing visual health.
        </p>

        <!--
          MAILING LIST:
          When a provider/endpoint is chosen, replace action="" below.
          Examples could be Mailchimp, Brevo, Formspree, or a custom endpoint.
        -->

        <form
          class="contact-form"
          action=""
          method="post"
        >

          <div class="contact-form-grid">

            <div class="form-field">
              <label for="full-name">
                Full Name <span aria-hidden="true">*</span>
              </label>

              <input
                id="full-name"
                name="full_name"
                type="text"
                placeholder="Enter your full name"
                autocomplete="name"
                required
              >
            </div>


            <div class="form-field">
              <label for="email">
                Email Address <span aria-hidden="true">*</span>
              </label>

              <input
                id="email"
                name="email"
                type="email"
                placeholder="Enter your email address"
                autocomplete="email"
                required
              >
            </div>


            <div class="form-field">
              <label for="phone">
                Contact Number
              </label>

              <input
                id="phone"
                name="phone"
                type="tel"
                placeholder="Enter your phone number"
                autocomplete="tel"
              >
            </div>


            <div class="form-field">
              <label for="institution">
                Institution <span aria-hidden="true">*</span>
              </label>

              <input
                id="institution"
                name="institution"
                type="text"
                placeholder="Enter your institution or organization"
                autocomplete="organization"
                required
              >
            </div>


            <div class="form-field form-field-full">
                <label for="research-area">
                    Research Area <span aria-hidden="true">*</span>
                </label>

                <select
                    id="research-area"
                    name="research_area"
                    required
                >
                    <option value="" selected disabled>
                    Select your research area
                    </option>

                    <option value="Circadian Rhythms & Sleep">
                    Circadian Rhythms &amp; Sleep
                    </option>

                    <option value="Visual Health & Perception">
                    Visual Health &amp; Perception
                    </option>

                    <option value="Lighting Design & Technology">
                    Lighting Design &amp; Technology
                    </option>

                    <option value="Sensor Technology & Wearables">
                    Sensor Technology &amp; Wearables
                    </option>

                    <option value="Data Science & Analytics">
                    Data Science &amp; Analytics
                    </option>

                    <option value="Clinical Research">
                    Clinical Research
                    </option>

                    <option value="Other">
                    Other
                    </option>
                </select>
</div>


            <div class="form-field form-field-full">
              <label for="message">
                Message (Optional)
              </label>

              <textarea
                id="message"
                name="message"
                rows="5"
                placeholder="Share any specific interests or questions"
              ></textarea>
            </div>

          </div>


          <label class="consent-field">
            <input
              type="checkbox"
              name="consent"
              value="yes"
              required
            >

            <span>
              I consent to receiving emails about GLC research, events, and opportunities.
              You can unsubscribe at any time.
            </span>
          </label>


          <button
            class="contact-submit"
            type="submit"
          >
            Join Our Mailing List
          </button>

        </form>
      </div>

    </div>


    <aside class="contact-sidebar">

      <section class="contact-side-card">
        <h2>Contact Information</h2>

        <p class="contact-side-intro">
          Reach out to us directly
        </p>

        <div class="contact-detail">

          <div class="contact-detail-icon" aria-hidden="true">
            <svg viewBox="0 0 24 24">
              <rect x="3" y="5" width="18" height="14" rx="2"></rect>
              <path d="m3 7 9 6 9-6"></path>
            </svg>
          </div>

          <div>
            <h3>Email</h3>

            <a href="mailto:e.tsukimori@tum.de">
              e.tsukimori@tum.de
            </a>
          </div>

        </div>


        <div class="contact-detail">

          <div class="contact-detail-icon" aria-hidden="true">
            <svg viewBox="0 0 24 24">
              <path d="M5 4h4l2 5-3 2a16 16 0 0 0 5 5l2-3 5 2v4a2 2 0 0 1-2 2C10 21 3 14 3 6a2 2 0 0 1 2-2z"></path>
            </svg>
          </div>

          <div>
            <h3>Phone</h3>

            <a href="tel:+498928924544">
              +49 (89) 289 24544
            </a>
          </div>

        </div>


        <div class="contact-detail">

          <div class="contact-detail-icon" aria-hidden="true">
            <svg viewBox="0 0 24 24">
              <path d="M12 21s6-5.2 6-11a6 6 0 1 0-12 0c0 5.8 6 11 6 11z"></path>
              <circle cx="12" cy="10" r="2"></circle>
            </svg>
          </div>

          <div>
            <h3>Address</h3>

            <address>
              Translational Sensory &amp; Circadian Neuroscience Unit<br>
              Technical University of Munich<br>
              Arcisstraße 21<br>
              80333 Munich, Germany
            </address>
          </div>

        </div>
      </section>


      <section class="contact-side-card">
        <h2>Office Hours</h2>

        <p>
          Monday - Friday: 9:00 AM - 5:00 PM CET
        </p>
      </section>


      <section class="contact-side-card">
        <h2>Follow Our Research</h2>

        <p>
          Stay connected with our latest findings and updates through our academic and
          social channels.
        </p>

       <div class="contact-social-links">

        <a
            class="contact-social-link"
            href="https://www.linkedin.com/in/spitschan/"
            target="_blank"
            rel="noopener noreferrer"
            aria-label="Global Light Commons on LinkedIn"
        >
            <svg viewBox="0 0 24 24" aria-hidden="true">
            <path d="M6 9v9"></path>
            <path d="M6 6.5v.01"></path>
            <path d="M10 18v-5a4 4 0 0 1 8 0v5"></path>
            <path d="M10 9v9"></path>
            </svg>

            <span>LinkedIn</span>
        </a>

        <a
            class="contact-social-link"
            href="https://tscnlab.github.io/LightLogR/"
            target="_blank"
            rel="noopener noreferrer"
            aria-label="LightLogR on GitHub"
        >
            <svg viewBox="0 0 24 24" aria-hidden="true">
            <path d="M12 2a10 10 0 0 0-3.16 19.49"></path>
            <path d="M15.16 21.49A10 10 0 0 0 12 2"></path>
            <path d="M9 19c-4 1.2-4-2-5-2"></path>
            <path d="M15 22v-3.5c0-1 .1-1.8-.5-2.5 2.7-.3 5.5-1.3 5.5-6A4.6 4.6 0 0 0 18.8 7c.1-.3.5-1.5-.1-3 0 0-1-.3-3.2 1.2a11 11 0 0 0-5.8 0C7.5 3.7 6.5 4 6.5 4c-.6 1.5-.2 2.7-.1 3A4.6 4.6 0 0 0 5 10c0 4.7 2.8 5.7 5.5 6-.4.4-.6.9-.7 1.4"></path>
            </svg>

            <span>GitHub - LightLogR</span>
        </a>

        <a
            class="contact-social-link"
            href="https://www.youtube.com/channel/UCTrGLi-baRDhagV8ckBFgPQ"
            target="_blank"
            rel="noopener noreferrer"
            aria-label="Global Light Commons on YouTube"
        >
            <svg viewBox="0 0 24 24" aria-hidden="true">
            <rect x="3" y="6" width="18" height="12" rx="4"></rect>
            <path d="m10 9 5 3-5 3z"></path>
            </svg>

            <span>YouTube</span>
        </a>

        </div>
      </section>

    </aside>

  </section>

</main>