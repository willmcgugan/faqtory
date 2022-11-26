
# Frequently Asked Questions 

{%- for question in questions %}
<details>  
  <a name="{{ question.slug }}"></a>
  <summary><b>{{ question.title }}</b></summary>
  <p>

  {{ question. body }}
</details>
{% endfor %}

