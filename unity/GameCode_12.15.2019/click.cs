using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;
using Mono.Data.Sqlite;
using System.Data;

public class click : MonoBehaviour
{
    // Start is called before the first frame update
    GameManager GM;
    GameObject o_GM;
    bool is_clicked = false;
    float alphaNum = 0.1f;

    void Start()
    {
        this.GetComponent<SpriteRenderer>().color = new Color(1, 1, 1, alphaNum);
        o_GM = GameObject.Find("GM");
        GM = o_GM.GetComponent<GameManager>();
        
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    void OnMouseDown()
    {
        if (is_clicked||GM.rest_times <= 0)
            return;
        else
        {
            this.GetComponent<SpriteRenderer>().color = new Color(1, 1, 1, 1);
            GM.setTimes(this.tag, 1);
            Debug.Log(this.tag + "被点击了");
            GM.getTimes(this.tag);
            if(GM.rest_times > 0) GM.rest_times--;
            GM.setText("REST TIMES:"+GM.rest_times);
            if (GM.rest_times <= 0)
            {
                GM.sqlInsert();
                GM.readSqlite();
            }
        }
        is_clicked = true;
    }
}
