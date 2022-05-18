# Backend


## Build and Run

At the project's root: `oc-iml/ $`

>`docker build -t p5 ./backend` 
>
>`docker run -e PORT=80 -p 80:80 p5`

copy `notebook/vectorizer` to `src/utils/vectorizer` (included in the Dockerfile)

## Deploy

Deploy on heroku

`$ heroku login`

`$ heroku container:login`


into module P5 folder (where docker file is)

`$ heroku container:push web -a ociml-module5 `

`$ heroku container:release web -a ociml-module5`

logs:

`heroku logs --tail -a ociml-module5`

scale down / up: 

`heroku ps:scale web=0 -a ociml-module5`
`heroku ps:scale web=1 -a ociml-module5`

## Use

deployed on heroku: 

<https://ociml-module5.herokuapp.com/docs/>


### Dev

`uvicorn main:app --reload`