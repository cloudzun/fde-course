/* GA4 for both FDE sites. See README.md for the required GA4 stream setting. */
(function () {
  "use strict";

  var measurementId = "G-DSM77VN7ZQ";
  // Do not send local previews or unrelated sites to the production property.
  if (window.location.protocol !== "https:" ||
      !/^(www\.)?cloudzun\.com$/.test(window.location.hostname) ||
      !/^\/(fde-course|fde-102)\//.test(window.location.pathname) ||
      window.__fdeAnalyticsInitialized) return;
  window.__fdeAnalyticsInitialized = true;

  window.dataLayer = window.dataLayer || [];
  function gtag() { window.dataLayer.push(arguments); }
  gtag("js", new Date());
  // We own page_view events. Also disable history-based page views in GA4.
  gtag("config", measurementId, { send_page_view: false });

  var previousPath;
  var previousLocation = document.referrer;
  function trackPage() {
    var path = window.location.pathname;
    // Same-page anchors / repeated mount notifications are not new page views.
    if (path === previousPath) return;
    var location = window.location.origin + path + window.location.search;
    gtag("event", "page_view", {
      send_to: measurementId,
      page_location: location,
      page_title: document.title,
      page_referrer: previousLocation
    });
    previousPath = path;
    previousLocation = location;
  }

  // Material emits once on subscription, then after each instant page render.
  if (typeof document$ !== "undefined") {
    document$.subscribe(trackPage);
  } else if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", trackPage, { once: true });
  } else {
    trackPage();
  }

  // Async loading (or a blocked Google request) never blocks reading the course.
  var script = document.createElement("script");
  script.async = true;
  script.src = "https://www.googletagmanager.com/gtag/js?id=" + measurementId;
  document.head.appendChild(script);
})();
