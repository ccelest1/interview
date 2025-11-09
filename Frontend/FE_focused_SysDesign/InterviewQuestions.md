# [ Frontend Interview Questions Mid/Senior Level ](https://www.youtube.com/watch?v=ILaXhmTraQ4)

## Cookies v Session Storage
- Cookie: 4kb, server and client
    * When making http request, also sending cookies
    * Token, auth, sync between browser
- Local Storage
    * Persisted for ever
    - Store app state (dark vs light theme)
- Session
    * form inputs, auto deleted when user closes tab

## Optimization Strategies
- React app client side rendered w/ bundler
    1. Polyfill code - look for different features in code like promises, spread operator -> then look at target browser -> does browser support js feature?
        * Adding new code to support or replace fts not supported by browsers
        * Tree shaking:
    2. Compression
        - gzip -> content negotiation -> decompress (reduce 70% of payload)
            * uglify, minification
            * source maps - map source code to code distributed (prod debugging)
    3. Code Splitting
        - only ship js as necessary then lazy load after initial load

## Image Optimization Strategies
- Ship min size -> No pixelation
- Once you have dimensions look at compression and image optimization
    * remove metadata, modify color space to optimize variance
- WebP
- CDN: Caching policy
- Lazy loading/load on scroll
- Specify width and height
- `srcSet`: ship various images depending on device/viewport -> load on various platforms

## Performance Challenges
- Tools and Practices
    * Linting
        - TS (EsLint)
    * Unit Test/e2e testing
    * Dep Scan
    * Lighthouse Sentry - see impacts of changes to web performance immediately

## XSS Attack
- Cross Site Scripting Attacks
    * Attacker persists js code into db and user fetches bad code
    * Sanitize input -> no js code persisted (detect, remove)
    * Never render html/js from user
    * React -> `__dangerouslySetHTML`

## CDN
- Content Delivery Network
* Get assets from edge location based on CDN -> resources obtained from more proximal location
- AWS CloudFront and Cloudflare as well as Azure CDN

## Micro-Frontends
- Frontend with various components -> as we have various engineers (split parts into indep apps)
- Shell will put various apps together with indep functionalities based on number of teams
- Criteria/Rationale
    * Wanting to split a large team
    * Issues with pipelines - other teams waiting to push fts based on work of others
