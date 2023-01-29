#include <stdio.h>
#include <string.h>

int bufferSize = 32;
char *name,*passwd,line[32];

int set(char *username,char *password)
{
    FILE *fp;
    int isPresent;
    isPresent = checkUsername(username);
    if(isPresent==1)
    {
        return -1;
    }
    fp=fopen("database.txt","a");
    
    if(fp!=NULL)
    {
        printf("File Opened");
        fprintf(fp,"%s %s\n",username,password);
        fclose(fp);
        return 1;
    }
    else
    {
        printf("File Not Opened");
        return 0;
    }
}

int checkUsername(char *username)
{
FILE *fp;
    char *tok;
    fp=fopen("database.txt","r");
    if(fp!=NULL)
    {
        int count=0,isName,isPasswd,isPresent;
        printf("File Opened\n");

        while(fgets(line,bufferSize,fp)!=NULL)
        {
                
            name=strtok(line," ");

            isName = strcmp(username,name);

           
            if(isName==0)
            {

                return 1;
            }
            else
            continue;

                
        }
        fclose(fp);
        return 0;
    }
}



int check(char *username,char *password)
{
FILE *fp;
    char *tok;
    fp=fopen("database.txt","r");
    if(fp!=NULL)
    {
        int count=0,isName,isPasswd,isPresent;
        printf("File Opened\n");

        while(fgets(line,bufferSize,fp)!=NULL)
        {
                
            name=strtok(line," ");

            isName = strcmp(username,name);
            passwd=strtok(NULL," ");
            passwd[strlen(passwd)-1]='\0';

            isPasswd = strcmp(password,passwd);

           
            if(isName==0 && isPasswd==0)
            {
                printf("Valid");
                return 1;
            }
            else
            continue;

                
        }
        fclose(fp);
        printf("NOT Valid");
        return 0;
    }
}

int main(int argc[],char* argv[])
{
    int ifCheck = strcmp(argv[1],"check");
    int ifSet = strcmp(argv[1],"set");
    if(ifSet==0)
    {
        return set(argv[2],argv[3]);
    }
    if(ifCheck==0)
    {
        return check(argv[2],argv[3]);
                
    }
}
