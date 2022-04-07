# Module P5

## Topic

<https://data.stackexchange.com/stackoverflow/query/new>



## Bibliography

<https://colah.github.io/posts/2015-08-Understanding-LSTMs/>

<https://openclassrooms.com/fr/courses/6532301-introduction-to-natural-language-processing>

## Build and Run

At the project's root: `oc-iml/ $`

> `cp requirements.txt modules/P5/evaluation`
>
>`docker build -t p5 ./modules/P5/evaluation/` 
>
>`docker run -p 80:80 p5`


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