
# Frequently Asked Questions 

{%- for question in questions %}
<details>  
  <summary><b>{{ question.title }}</b></summary>
  <p>

  {{ question. body }}
</details>
{% endfor %}

